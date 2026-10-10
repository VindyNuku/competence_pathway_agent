
# AI-assisted learning pathway explanations

from ollama import chat

from competencies import identify_skill_gaps
from learning_resources import recommend_learning_path
from explanations import explain_recommendations


def generate_ai_advice(current_skills, career_goal):
    gaps = identify_skill_gaps(current_skills, career_goal)
    pathway = recommend_learning_path(gaps)
    explanations = explain_recommendations(gaps)

    if not gaps:
        return "No missing competencies in the selected career profile."

    recommendations = "\n".join(
        f"- {item['competency']}: "
        f"{item['learning_resource']}. "
        f"Reason: {explanations[item['competency']]}"
        for item in pathway
    )

    response = chat(
        model="qwen3.5:2b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a supportive lifelong learning advisor. "
                    "Use only the provided competency information. "
                    "Explain why each recommended skill matters "
                    "and how it connects to the learner's existing skills. "
                    "Do not invent courses, qualifications, or skill gaps. "
                    "Keep the response brief and clear."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Career goal: {career_goal}\n"
                    f"Existing skills: {', '.join(current_skills)}\n"
                    f"Recommended pathway:\n{recommendations}\n\n"
                    "Explain this learning pathway to the learner."
                ),
            },
        ],
        options={"temperature": 0},
    )

    return response.message.content


if __name__ == "__main__":
    skills = ["Python", "Excel", "Communication"]

    print("Generating AI learning advice...\n")

    advice = generate_ai_advice(
        skills,
        "Junior Data Analyst"
    )

    print(advice)
