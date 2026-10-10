
# Tiny AI Competence & Learning Pathway Agent
# Step 1: Define the target career competencies

CAREER_PROFILES = {
    "Junior Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Statistics",
        "Power BI",
        "Communication"
    ]
}


def identify_skill_gaps(current_skills, career_goal):
    required_skills = CAREER_PROFILES[career_goal]

    current = {skill.lower() for skill in current_skills}

    missing = [
        skill for skill in required_skills
        if skill.lower() not in current
    ]

    return missing


# Quick test
if __name__ == "__main__":
    learner_skills = ["Python", "Excel", "Communication"]

    gaps = identify_skill_gaps(
        learner_skills,
        "Junior Data Analyst"
    )

    print("Existing skills:", learner_skills)
    print("Missing competencies:", gaps)
