import os

import streamlit as st
from app.context import load_context
from app.prompts import build_system_instruction
from groq import Groq


@st.cache_resource
def _get_groq_client() -> Groq:
    return Groq(api_key=os.environ.get("GROQ_API_KEY"))


def generate_ai_response(prompt: str, chat_history: list | None = None) -> str:
    client = _get_groq_client()
    context = load_context()
    model = os.environ.get("AI_MODEL_NAME") or "llama-3.1-8b-instant"

    system_instruction = build_system_instruction(context)

    messages = [
        {"role": "system", "content": system_instruction},
        *({"role": m["role"], "content": m["content"]} for m in (chat_history or [])),
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        messages=messages,  # type: ignore[arg-type]
        model=model,
        max_tokens=500,
    )
    return (response.choices[0].message.content or "").strip()
