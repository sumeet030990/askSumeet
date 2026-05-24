import os
import streamlit as st

_MYINFO_DIR = os.path.join(os.path.dirname(__file__), "..", "myInfo")


@st.cache_resource
def load_context() -> str:
    parts = []
    for filename in sorted(os.listdir(_MYINFO_DIR)):
        filepath = os.path.join(_MYINFO_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            parts.append(f.read())
    return "\n\n".join(parts)
