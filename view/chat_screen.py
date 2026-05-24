import streamlit as st
from app.state_management import make_message
from app.ai import generate_ai_response
from app.logger import log_message
from app.notifications import send_message_notification, send_direct_message_notification

def _render_contact_widget(session_id: str, profile: dict) -> None:
    with st.container(border=True):
        st.markdown("**Send Sumeet a message**")
        st.caption("He'll receive a push notification and get back to you.")
        msg = st.text_area(
            "Your message",
            key="contact_widget_message",
            placeholder="Hi Sumeet, I'd love to connect...",
            height=100,
            label_visibility="collapsed",
        )
        if st.button("Send Message", type="primary", key="contact_widget_send"):
            if msg.strip():
                send_direct_message_notification(session_id, profile, msg.strip())
                st.session_state["show_contact_widget"] = False
                st.session_state["contact_message_sent"] = True
                st.rerun()
            else:
                st.warning("Please enter a message before sending.")

def load_chat_screen():
    st.write("You can ask about Sumeet Personal and Professional details, his work experience, education, skills, projects, and more.")
    profile = st.session_state.get("user_profile", {"name": "", "phone": "", "email": ""})
    st.caption(
        f"Session for {profile['name']}"
        + (f" | Email: {profile['email']}" if profile["email"] else "")
        + (f" | Phone: {profile['phone']}" if profile["phone"] else "")
    )

    if st.session_state.pop("contact_message_sent", False):
        st.toast("Your message was sent to Sumeet!", icon="✅")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("New Session"):
            st.session_state["session_started"] = False
            st.session_state["session_id"] = ""
            st.session_state["user_profile"] = {"name": "", "phone": "", "email": ""}
            st.session_state["messages"] = []
            st.session_state["show_contact_widget"] = False
            st.rerun()
    with col2:
        if st.button("Clear Chat"):
            st.session_state["messages"] = []
            st.session_state["show_contact_widget"] = False
            st.rerun()

    session_id = st.session_state.get("session_id", "")

    for message in st.session_state.get("messages", []):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if st.session_state.get("show_contact_widget"):
        _render_contact_widget(session_id, profile)

    prompt = st.chat_input("Ask about Sumeet...")
    if not prompt:
        return

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    user_msg = make_message("user", prompt)
    st.session_state["messages"].append(user_msg)
    log_message(session_id, user_msg)

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply, show_contact_form = generate_ai_response(prompt, chat_history=st.session_state.get("messages", []))
        st.markdown(reply)

    assistant_msg = make_message("assistant", reply)
    st.session_state["messages"].append(assistant_msg)
    log_message(session_id, assistant_msg)
    send_message_notification(session_id, profile, f"{profile['name']}: {prompt}\nAI: {reply}")

    if show_contact_form:
        st.session_state["show_contact_widget"] = True
        st.rerun()
