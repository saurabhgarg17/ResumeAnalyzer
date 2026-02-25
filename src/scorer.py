def calculate_match_score_old(resume_skills, jd_skills):
    if not jd_skills:
        return 0
    return round((len(resume_skills & jd_skills) / len(jd_skills)) * 100, 2)

def calculate_match_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0.0

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched = resume_set & jd_set
    score = (len(matched) / len(jd_set)) * 100

    return round(score, 2)