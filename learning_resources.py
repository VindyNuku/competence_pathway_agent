
# Example learning resources for our prototype
# These are fictional resources, not real courses.

LEARNING_RESOURCES = {
    "Python": "Python for Data Analysis",
    "SQL": "SQL Fundamentals",
    "Excel": "Excel for Business Analytics",
    "Statistics": "Introduction to Statistics",
    "Power BI": "Power BI Dashboard Basics",
    "Communication": "Communicating Data Insights"
}


def recommend_learning_path(missing_skills):
    pathway = []

    for step, skill in enumerate(missing_skills, start=1):
        pathway.append({
            "step": step,
            "competency": skill,
            "learning_resource": LEARNING_RESOURCES[skill]
        })

    return pathway


if __name__ == "__main__":
    from competencies import identify_skill_gaps

    learner_skills = ["Python", "Excel", "Communication"]

    gaps = identify_skill_gaps(
        learner_skills,
        "Junior Data Analyst"
    )

    pathway = recommend_learning_path(gaps)

    print("\nYour personalised learning pathway:\n")

    for item in pathway:
        print(
            f"Step {item['step']}: "
            f"Learn {item['competency']} "
            f"→ {item['learning_resource']}"
        )
