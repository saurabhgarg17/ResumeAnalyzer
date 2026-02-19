import streamlit as st
import pdfplumber
from docx import Document
import spacy
from src.skill_extractor import load_skills, extract_skills
from src.scorer import calculate_match_score

nlp = spacy.load("en_core_web_lg")

def clean_text(text):
    doc = nlp(text.lower())
    return " ".join(
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct
    )

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join(p.text for p in doc.paragraphs)

st.set_page_config(page_title="Smart Resume Analyzer", layout="centered")

st.title("🧠 Smart Resume Analyzer")
st.write("Analyze how well a resume matches a job description using Python & NLP.")

st.divider()

resume_file = st.file_uploader(
    "📄 Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "📝 Paste Job Description",
    height=200,
    placeholder="Paste the full job description here..."
)

analyze_btn = st.button("🔍 Analyze Resume")

if analyze_btn:
    if not resume_file or not job_description.strip():
        st.warning("Please upload a resume and paste a job description.")
    else:
        with st.spinner("Analyzing resume..."):
            # Resume extraction
            if resume_file.name.endswith(".pdf"):
                resume_text = extract_text_from_pdf(resume_file)
            else:
                resume_text = extract_text_from_docx(resume_file)

        resume_clean = clean_text(resume_text)
        jd_clean = clean_text(job_description)
        print("resume_clean:", resume_clean)
        print("jd_clean:", jd_clean)
        skills = load_skills()


        resume_skills = extract_skills(resume_clean, skills)
        jd_skills = extract_skills(jd_clean, skills)

        print("resume_skills:", resume_skills)
        print("jd_skills:", jd_skills)

        # Scoring
        score = calculate_match_score(resume_skills, jd_skills)
        matched = resume_skills & jd_skills
        missing = jd_skills - resume_skills

        st.success("Analysis Complete ✅")

        st.subheader("📊 Match Score")
        st.metric(label="Resume Match", value=f"{score}%")

        st.subheader("✅ Matched Skills")
        if matched:
            st.write(", ".join(sorted(matched)))
        else:
            st.write("No matched skills found.")

        st.subheader("❌ Missing Skills")
        if missing:
            st.write(", ".join(sorted(missing)))
        else:
            st.write("No missing skills 🎉")

        st.divider()
        st.info("💡 Tip: Consider adding missing skills to improve your resume alignment.")