
# Feature 4: Explainable competence recommendations

from competencies import identify_skill_gaps
from learning_resources import recommend_learning_path

SKILL_EXPLANATIONS = {
    "Python": "Python helps analysts automate data processing and analysis.",
    "SQL": "SQL helps analysts retrieve and analyse data stored in databases.",
    "Excel": "Excel supports data cleaning, calculations and business reporting.",
    "Statistics": "Statistics helps analysts interpret data and draw evidence-based conclusions.",
    "Power BI": "Power BI helps analysts create dashboards and communicate insights.",
    "Communication": "Communication helps analysts explain findings to different audiences."
}


def explain_recommendations(missing_skills):
    return {
        skill: SKILL_EXPLANATIONS.get(
            skill, "This skill is part of the target career profile."
        )
        for skill in missing_skills
    }


if __name__ == "__main__":
    learner_skills = ["Python", "Excel", "Communication"]
    career_goal = "Junior Data Analyst"

    gaps = identify_skill_gaps(learner_skills, career_goal)
    pathway = recommend_learning_path(gaps)
    explanations = explain_recommendations(gaps)

    print("\nYOUR EXPLAINABLE LEARNING PATHWAY\n")

    for item in pathway:
        skill = item["competency"]

        print(f"Step {item['step']}: {skill}")
        print(f"Resource: {item['learning_resource']}")
        print(f"Why: {explanations[skill]}\n")
