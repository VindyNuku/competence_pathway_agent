
import json
from ollama import chat

from competencies import identify_skill_gaps
from learning_resources import recommend_learning_path
from explanations import explain_recommendations


def analyse_learning_needs(current_skills: list[str], career_goal: str) -> dict:
    """Identify missing competencies and return a grounded learning pathway."""
    gaps = identify_skill_gaps(current_skills, career_goal)
    pathway = recommend_learning_path(gaps)
    explanations = explain_recommendations(gaps)

    return {
        "career_goal": career_goal,
        "existing_skills": current_skills,
        "missing_skills": gaps,
        "learning_pathway": [
            {
                **item,
                "why": explanations[item["competency"]]
            }
            for item in pathway
        ]
    }


TOOLS = {
    "analyse_learning_needs": analyse_learning_needs
}


def run_agent(current_skills, career_goal):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a lifelong learning assistant. "
                "Use the analyse_learning_needs tool to obtain "
                "competency gaps and learning recommendations. "
                "Do not invent skills or learning resources. "
                "Explain the results briefly and clearly."
            )
        },
        {
            "role": "user",
            "content": (
                f"My existing skills are: {', '.join(current_skills)}. "
                f"My career goal is {career_goal}. "
                "Identify my gaps and explain my learning pathway."
            )
        }
    ]

    response = chat(
        model="qwen3.5:2b",
        messages=messages,
        tools=[analyse_learning_needs],
        options={"temperature": 0}
    )

    messages.append(response.message)

    if not response.message.tool_calls:
        return "The model did not request the competence analysis tool."

    for tool_call in response.message.tool_calls:
        name = tool_call.function.name

        if name not in TOOLS:
            return f"Unsupported tool requested: {name}"

        arguments = tool_call.function.arguments

        if isinstance(arguments, str):
            arguments = json.loads(arguments)

        result = TOOLS[name](**arguments)

        messages.append({
            "role": "tool",
            "tool_name": name,
            "content": json.dumps(result)
        })

    final_response = chat(
        model="qwen3.5:2b",
        messages=messages,
        options={"temperature": 0}
    )

    return final_response.message.content


if __name__ == "__main__":
    print("Running our first tool-calling agent...\n")

    answer = run_agent(
        ["Python", "Excel", "Communication"],
        "Junior Data Analyst"
    )

    print(answer)
