import streamlit as st
from view.chat_screen import load_chat_screen
from view.registration_form import load_registration_form
from app.state_management import initialize_session_state


def initialize_ui():
    initialize_session_state()

    st.markdown("<h1 style='text-align: center;'>Ask Sumeet</h1>", unsafe_allow_html=True)

    if not st.session_state.get("session_started", False):
        load_registration_form()
    else:
        load_chat_screen()