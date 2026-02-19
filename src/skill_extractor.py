
import csv

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

def extract_skills(text, skills):
    found = set()

    for skill in skills:
        if skill in text:
            found.add(skill)
    return found
