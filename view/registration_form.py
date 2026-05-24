import streamlit as st
from uuid import uuid4

def load_registration_form():
    st.write("Please enter your details to begin chatting.")

    with st.form("intake_form"):
        name = st.text_input("Name *")
        phone = st.text_input("Phone (optional)")
        email = st.text_input("Email (optional)")
        submitted = st.form_submit_button("Start Session")

        if submitted:
            st.session_state["session_started"] = True
            st.session_state["session_id"] = str(uuid4())
            st.session_state["user_profile"] = {"name": name, "phone": phone, "email": email}
            st.rerun()
        