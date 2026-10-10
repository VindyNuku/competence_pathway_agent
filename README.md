# AI Competence & Learning Pathway Assistant

A small **agentic AI prototype** exploring how artificial intelligence and competence analytics can support personalised lifelong learning.

The application identifies competency gaps, recommends learning pathways, explains its recommendations, and adapts when learners update their skills.

## Project Overview

This prototype demonstrates a simple AI-supported learning pathway for a predefined career goal: **Junior Data Analyst**.

Learners select their existing competencies, and the system compares them with an example career profile to identify missing skills.

A locally running AI model then generates personalised learning advice.

## Key Features

- **Competency gap analysis:** Identifies missing skills based on the selected career profile.
- **AI-generated recommendations:** Explains why missing competencies matter and suggests learning resources.
- **Adaptive learning pathways:** Updates recommendations when learners complete competencies.
- **Competency coverage indicator:** Displays progress against the example career profile.
- **Explainable recommendations:** Provides reasons for each suggested learning step.
- **Learner feedback:** Allows users to indicate whether a recommendation was helpful.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Ollama | Runs a language model locally |
| Qwen | Generates learning advice |
| Gradio | Interactive web interface |

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/VindyNuku/competence_pathway_agent.git
cd competence_pathway_agent
```

### 2. Create a Python environment

Using Conda:

```bash
conda create -n competence-agent python=3.11
conda activate competence-agent
```

### 3. Install dependencies

```bash
pip install gradio==6.26.0 ollama
```

### 4. Install and configure Ollama

Install Ollama from https://ollama.com/.

Download the language model:

```bash
ollama pull qwen3.5:2b
```

Ensure Ollama is running locally.

### 5. Start the application

```bash
python app.py
```

Open the local address displayed in your terminal, typically:

http://127.0.0.1:7860

## How to Use

1. Select your existing competencies.
2. Review your competency coverage indicator.
3. Click **Analyse My Skills** to identify gaps and generate recommendations.
4. Mark a competency as completed to update your learning pathway.
5. Provide feedback using **Helpful** or **Not Helpful**.

## Project Structure

```text
competence_pathway_agent/
├── agent.py
├── ai_advisor.py
├── app.py
├── competencies.py
├── explanations.py
├── learner_progress.py
├── learning_resources.py
├── Screenshots/
├── .gitignore
└── README.md
```

## Research Context

This prototype is an early exploration of the research topic:

**From Learning Data to Future Skills: Using Agentic AI and Competence Analytics to Support Lifelong Learning**

It demonstrates how AI-supported competence analysis, explainable recommendations, learner progress, and feedback could contribute to adaptive lifelong learning systems.

## Current Limitations

- Uses a predefined Junior Data Analyst competency profile.
- Uses fictional learning resources for demonstration.
- Competencies are self-reported rather than independently assessed.
- The progress indicator represents profile coverage, not verified career readiness.
- Learner feedback is acknowledged in the interface but is not yet stored or used to improve recommendations.
- The prototype has not been formally evaluated with learners.

## Future Development

Potential improvements include integrating real learning resources, supporting additional career profiles, recording learner feedback, and evaluating recommendation quality, transparency, and learner experience.

## Project Status

**Version 1.0 - Early research prototype**

Developed as a personal learning and research demonstration using Python, Ollama, and Gradio.