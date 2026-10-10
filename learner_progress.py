
# Feature 3: Adaptive learning pathway

from competencies import identify_skill_gaps
from learning_resources import recommend_learning_path


def update_learner_progress(current_skills, completed_skill):
    updated_skills = current_skills.copy()

    if completed_skill.lower() not in {
        skill.lower() for skill in updated_skills
    }:
        updated_skills.append(completed_skill)

    return updated_skills


if __name__ == "__main__":
    career_goal = "Junior Data Analyst"
    learner_skills = ["Python", "Excel", "Communication"]

    print("BEFORE completing SQL:")
    gaps = identify_skill_gaps(learner_skills, career_goal)

    for item in recommend_learning_path(gaps):
        print(f"Step {item['step']}: {item['competency']}")

    # Learner reports completing SQL
    learner_skills = update_learner_progress(
        learner_skills, "SQL"
    )

    print("\nAFTER completing SQL:")
    gaps = identify_skill_gaps(learner_skills, career_goal)

    for item in recommend_learning_path(gaps):
        print(f"Step {item['step']}: {item['competency']}")

    print("\nUpdated learner skills:", learner_skills)
