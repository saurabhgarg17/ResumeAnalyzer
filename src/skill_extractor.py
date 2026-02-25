
import csv
import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_lg")

def load_skills(path="data/skills.csv"):
    skills = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)  # Handles CSV parsing
        for row in reader:
            if not row:
                continue  # Skip empty lines
            skill = row[0].strip().lower()  # Take first column, remove whitespace
            if skill:
                skills.append(skill)
    return skills

def extract_skills_old(text, skills):
    found = set()

    for skill in skills:
        if skill in text:
            found.add(skill)
    return found

def extract_skills(text, skills):
    doc = nlp(text.lower())

    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(skill) for skill in skills]
    matcher.add("SKILLS", patterns)

    matches = matcher(doc)

    found_skills = set()
    for _, start, end in matches:
        found_skills.add(doc[start:end].text)

    return sorted(found_skills)