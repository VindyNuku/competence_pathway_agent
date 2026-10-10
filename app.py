
import gradio as gr

from agent import run_agent
from competencies import CAREER_PROFILES, identify_skill_gaps
from learner_progress import update_learner_progress

CAREER_GOAL = "Junior Data Analyst"
ALL_SKILLS = CAREER_PROFILES[CAREER_GOAL]


def analyse_skills(current_skills):
    current_skills = current_skills or []
    gaps = identify_skill_gaps(current_skills, CAREER_GOAL)

    summary = (
        f"**Existing competencies:** {', '.join(current_skills) or 'None'}\n\n"
        f"**Missing competencies:** {', '.join(gaps) or 'None'}"
    )

    if not gaps:
        return summary, "All competencies in this example profile are covered."

    try:
        advice = run_agent(current_skills, CAREER_GOAL)
    except Exception as error:
        advice = f"AI advice could not be generated: {error}"

    return summary, advice


def complete_skill(current_skills, completed_skill):
    current_skills = current_skills or []

    if not completed_skill:
        return current_skills, "Please select a skill to mark as completed."

    updated = update_learner_progress(
        current_skills, completed_skill
    )

    return updated, f"Marked **{completed_skill}** as completed. Click **Analyse My Skills** to update your pathway."



def show_progress(current_skills):
    current_skills = current_skills or []

    covered = len(set(current_skills) & set(ALL_SKILLS))
    total = len(ALL_SKILLS)
    percentage = round((covered / total) * 100)

    return f"""
    <div style="padding:16px;">
        <h3 style="color:#243B53; margin-bottom:8px;">
            Competency Profile Coverage
        </h3>

        <p style="color:#243B53;">
            <strong>{covered} of {total} competencies selected — {percentage}%</strong>
        </p>

        <div style="background:#E2F0FC; border-radius:12px;
                    height:18px; overflow:hidden;">
            <div style="background:#5B8FB9; width:{percentage}%;
                        height:100%; border-radius:12px;">
            </div>
        </div>

        <p style="font-size:13px; color:#37658C; margin-top:10px;">
            Progress against the example career profile,
            not a verified measure of career readiness.
        </p>
    </div>
    """

cool_blue = gr.themes.Color(
    name="cool_blue",
    c50="#F0F7FF",
    c100="#E2F0FC",
    c200="#C9E4F7",
    c300="#A8D5F2",
    c400="#83B9DE",
    c500="#5B8FB9",
    c600="#477CA7",
    c700="#37658C",
    c800="#2B506F",
    c900="#243B53",
    c950="#172A3B",
)

theme = gr.themes.Soft(
    primary_hue=cool_blue,
    secondary_hue=gr.themes.colors.blue,
    neutral_hue=gr.themes.colors.slate,
).set(
    body_background_fill="#F0F7FF",
    block_background_fill="#FFFFFF",
    block_label_text_color="#37658C",
    body_text_color="#243B53",
    button_primary_background_fill="#A8D5F2",
    button_primary_background_fill_hover="#83B9DE",
    button_primary_text_color="#243B53",
    input_background_fill="#FFFFFF",
    input_border_color="#C9E4F7",
)

with gr.Blocks(
    title="AI Competence & Learning Pathway Assistant",
    theme=theme
) as demo:
    gr.Markdown(
        "# AI Competence & Learning Pathway Assistant\n"
        "A tiny agentic AI prototype for personalised lifelong learning.\n\n"
        "**Research demonstration: uses fictional learning resources and "
        "a predefined career profile.**"
    )

    gr.Markdown("### Your learner profile")

    career_goal = gr.Textbox(
        label="Career goal",
        value=CAREER_GOAL,
        interactive=False
    )

    skills = gr.CheckboxGroup(
        choices=ALL_SKILLS,
        value=["Python", "Excel", "Communication"],
        label="Select your existing competencies"
    )

    
    progress_display = gr.HTML(
        value=show_progress(["Python", "Excel", "Communication"])
    )

    skills.change(
        fn=show_progress,
        inputs=skills,
        outputs=progress_display
    )


    analyse_button = gr.Button(
        "Analyse My Skills",
        variant="primary"
    )

    summary = gr.Markdown(label="Competence analysis")
    advice = gr.Markdown(label="AI learning pathway")

    analyse_button.click(
        fn=analyse_skills,
        inputs=skills,
        outputs=[summary, advice]
    )

    gr.Markdown("### Update your learning progress")

    completed_skill = gr.Dropdown(
        choices=ALL_SKILLS,
        label="Competency completed",
        value=None
    )

    complete_button = gr.Button("Mark Skill as Completed")
    progress_message = gr.Markdown()

    complete_button.click(
        fn=complete_skill,
        inputs=[skills, completed_skill],
        outputs=[skills, progress_message]
    ).then(
        fn=show_progress,
        inputs=skills,
        outputs=progress_display
    ).then(
        fn=analyse_skills,
        inputs=skills,
        outputs=[summary, advice]
    )


demo.launch(inbrowser=True)
