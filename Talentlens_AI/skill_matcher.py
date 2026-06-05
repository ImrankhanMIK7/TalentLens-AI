MARKET_SKILLS = {
    "data analysis",
    "sql",
    "python",
    "excel",
    "tableau",
    "power bi",
    "business analysis",
    "reporting",
    "problem solving",
    "business intelligence",
    "data analytics",
    "data visualization",
    "statistics",
    "machine learning",
    "project management",
    "communication",
    "data modeling",
    "data warehousing",
    "jira",
    "agile",
    "postgresql",
    "git",
    "github",
    "pandas",
    "numpy",
    "scikit-learn"
}


def extract_skills(text):
    found = []

    for skill in MARKET_SKILLS:
        if skill in text:
            found.append(skill)

    return sorted(found)


def calculate_score(found_skills):

    matched = set(found_skills)

    missing = MARKET_SKILLS - matched

    score = round(
        len(matched) / len(MARKET_SKILLS) * 100,
        2
    )

    return score, matched, missing