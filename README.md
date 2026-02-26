# Resume Analyzer

Python-based resume analyzer that compares resumes with job descriptions using NLP.This project is built as a learning-focused.

## Running

As this program runs on python 3.11 you need to create a virtual environment if you are running higher version. 
Switch to working directory and create environment.
```bash
py -3.11 -m venv venv
venv\Scripts\activate
```
Install supporting libraries 
```bash
pip install streamlit pdfplumber python-docx spacy pandas
python -m spacy download en_core_web_sm
```
Run Program
```bash
python -m streamlit run ui.py
```
## Usage
Upload resume in word or pdf format. Add Job description in text area and click on Analyze Resume.


## Tech Stack
**Language**
* Python 3.11

**NLP**
* spaCy (en_core_web_lg)
* PhraseMatcher (multi-word technical skills)

**Data Processing**
* pdfplumber – PDF parsing
* python-docx – DOCX parsing
* CSV-based skill dictionary (skills.csv)

**Frontend**
* Streamlit

## Planned Enhancements
* Detect resume sections (Skills, Experience, Projects)
* Weight skills based on where they appear and years of experience
* Infer implicit skills from experience descriptions
* Detect technologies not explicitly listed
* Exportable evaluation reports

## Contributing

Pull requests are welcome. 
