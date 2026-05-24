import streamlit as st
from uuid import uuid4
from app.logger import log_session_start
from app.notifications import send_session_notification

def load_registration_form():
    st.write("Please enter your details to begin chatting.")

    with st.form("intake_form"):
        name = st.text_input("Name *")
        phone = st.text_input("Phone (optional)")
        email = st.text_input("Email (optional)")
        submitted = st.form_submit_button("Start Session")

        if submitted:
            session_id = str(uuid4())
            user_profile = {"name": name, "phone": phone, "email": email}
            st.session_state["session_started"] = True
            st.session_state["session_id"] = session_id
            st.session_state["user_profile"] = user_profile
            log_session_start(session_id, user_profile)
            send_session_notification(session_id, user_profile)
            st.rerun()
        