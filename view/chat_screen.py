import streamlit as st
from app.state_management import make_message
from app.ai import generate_ai_response
from app.logger import log_message

def load_chat_screen():
    st.write("You can ask about Sumeet Personal and Professional details, his work experience, education, skills, projects, and more.")
    profile = st.session_state.get("user_profile", {"name": "", "phone": "", "email": ""})
    st.caption(
        f"Session for {profile['name']}"
        + (f" | Email: {profile['email']}" if profile["email"] else "")
        + (f" | Phone: {profile['phone']}" if profile["phone"] else "")
    )
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("New Session"):
            st.session_state["session_started"] = False
            st.session_state["session_id"] = ""
            st.session_state["user_profile"] = {"name": "", "phone": "", "email": ""}
            st.session_state["messages"] = []
            st.rerun()
    with col2:
        if st.button("Clear Chat"):
            st.session_state["messages"] = []
            st.write("Chat cleared. Ask me anything about Sumeet.")
            st.rerun()
    
    
    for message in st.session_state.get("messages", []):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    prompt = st.chat_input("Ask about Sumeet...")
    if not prompt:
        return

    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    session_id = st.session_state.get("session_id", "")

    user_msg = make_message("user", prompt)
    st.session_state["messages"].append(user_msg)
    log_message(session_id, user_msg)

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = str(st.write_stream(generate_ai_response(prompt, chat_history=st.session_state.get("messages", []))))

    assistant_msg = make_message("assistant", reply)
    st.session_state["messages"].append(assistant_msg)
    log_message(session_id, assistant_msg)
