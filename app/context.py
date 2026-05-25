import os
import streamlit as st

_MYINFO_DIR = os.path.join(os.path.dirname(__file__), "..", "myInfo")


_CONTEXT_CHAR_LIMIT = 18_000  # ~4,500 tokens, leaves budget for prompt + history + reply


@st.cache_resource
def load_context() -> str:
    parts = []
    for filename in sorted(os.listdir(_MYINFO_DIR)):
        if filename.lower() == "readme.md":
            continue
        filepath = os.path.join(_MYINFO_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            parts.append(f.read())
    context = "\n\n".join(parts)
    return context[:_CONTEXT_CHAR_LIMIT]
