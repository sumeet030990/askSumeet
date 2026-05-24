# Sumeet Jadhav – Virtual AI Knowledge Base

This is the structured knowledge base for Sumeet's virtual AI assistant.
Each file is kept focused so it can be retrieved accurately (RAG-friendly).

---

## File Map

```
/professional
  experience.md     ← Work history, companies, roles, durations
  projects.md       ← Detailed project breakdowns with responsibilities
  skills.md         ← Technical + soft skills with context
  education.md      ← Degrees, certifications, current learning

/personal
  about.md          ← Identity, personality, working style, aspirations
  faq.md            ← ⭐ Q&A pairs — most important file for AI quality

/context
  opinions.md       ← Views on tech, AI, work — gives the AI your voice
```

---

## How to Use This

### Option 1: System Prompt Injection (simplest)
Concatenate all files into one string and pass as the system prompt:
```
You are a virtual version of Sumeet Jadhav. Answer questions based only on the information below.
[paste all file contents here]
```

### Option 2: RAG (Retrieval-Augmented Generation) — recommended at scale
- Chunk each file into sections
- Embed with OpenAI/Cohere/local embeddings
- Store in a vector DB (Pinecone, Supabase, ChromaDB)
- Retrieve top-k relevant chunks per user question

### Option 3: Fine-tuning (later stage)
Convert `faq.md` entries into JSONL prompt-completion pairs for fine-tuning.

---

## How to Keep This Growing

| What happened | Where to add it |
|---|---|
| New job / promotion | `experience.md` + `projects.md` |
| New skill learned | `skills.md` |
| New certification | `education.md` |
| Common interview question | `faq.md` |
| Changed opinion on a technology | `opinions.md` |
| Personal milestone | `about.md` |

---

## Priority: Fill These First
1. `faq.md` – complete the placeholder answers in your own words
2. `opinions.md` – add your tech opinions and philosophy
3. `projects.md` – add more detail/impact metrics to each project if you remember them
