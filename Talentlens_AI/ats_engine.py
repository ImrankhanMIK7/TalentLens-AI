from .resume_parser import extract_text
from .skill_matcher import extract_skills

MARKET_SKILLS = {
    "sql",
    "python",
    "excel",
    "tableau",
    "power bi",
    "data analysis",
    "data visualization",
    "business analysis",
    "reporting",
    "business intelligence"
}


def ats_score(pdf_path):

    text = extract_text(pdf_path)

    resume_skills = set(
        extract_skills(text)
    )

    matched = resume_skills.intersection(
        MARKET_SKILLS
    )

    missing = MARKET_SKILLS - resume_skills

    score = (
        len(matched)
        / len(MARKET_SKILLS)
    ) * 100

    return score, matched, missing