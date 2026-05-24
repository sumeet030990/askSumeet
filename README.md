# Ask Sumeet

A conversational AI assistant that lets anyone ask questions about Sumeet Jadhav — his work experience, skills, projects, education, and more. Built with Streamlit and powered by Groq.

## What it does

- Answers questions about Sumeet in first person, grounded strictly in his knowledge base
- Maintains chat history within a session for context-aware follow-ups
- Collects a brief visitor profile (name, optional email/phone) before starting the session
- Reads all context from `/myInfo` markdown files — no redeployment needed to update content

## Project structure

```
AskSumeet/
├── main.py                   # Streamlit entry point
├── app/
│   ├── ai.py                 # Groq API call + system instruction
│   ├── context.py            # Loads and joins myInfo/*.md into a single context string
│   └── state_management.py   # Session state helpers
├── view/
│   ├── ui.py                 # Top-level UI router (registration vs chat)
│   ├── registration_form.py  # Visitor intake form
│   └── chat_screen.py        # Chat UI and message loop
└── myInfo/
    ├── about.md
    ├── experience.md
    ├── projects.md
    ├── skills.md
    ├── education.md
    ├── faq.md
    └── opinions.md
```

## Setup

**Prerequisites:** Python 3.13+, [uv](https://github.com/astral-sh/uv)

```bash
# Install dependencies
uv sync

# Copy and fill in environment variables
cp .env.example .env
```

**.env**
```
GROQ_API_KEY=your_groq_api_key
AI_MODEL_NAME=llama-3.1-8b-instant   # any Groq-supported model
```

## Running

```bash
uv run streamlit run main.py
```

Then open [http://localhost:8501](http://localhost:8501).

## Setting up your knowledge base

Create a `myInfo/` folder at the project root and populate it with `.md` files about yourself. The AI reads every `.md` file in that folder and uses the combined content as its sole source of truth — no redeployment needed when you update a file.

### Recommended file structure

```
myInfo/
├── about.md        # Who you are — identity, personality, career aspirations
├── experience.md   # Work history: companies, roles, durations, responsibilities
├── projects.md     # Key projects with tech stack, your role, and outcomes
├── skills.md       # Technical and soft skills with context
├── education.md    # Degrees, certifications, courses in progress
├── faq.md          # Q&A pairs in your own words — most impactful file for AI quality
└── opinions.md     # Your views on tech, work style, and career — gives the AI your voice
```

### Keeping it up to date

| When this happens | Update this file |
|---|---|
| New job or promotion | `experience.md` + `projects.md` |
| New skill or certification | `skills.md` or `education.md` |
| Common question in an interview | `faq.md` |
| Changed opinion on a technology | `opinions.md` |

## Tech stack

- [Streamlit](https://streamlit.io) — UI framework
- [Groq](https://groq.com) — LLM inference (fast, low-latency)
- [uv](https://github.com/astral-sh/uv) — Python package manager
