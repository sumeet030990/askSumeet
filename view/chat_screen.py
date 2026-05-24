import streamlit as st
from app.state_management import make_message
from app.ai import generate_ai_response

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
    st.session_state["messages"].append(make_message("user", prompt))
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    reply = generate_ai_response(prompt, chat_history=st.session_state.get("messages", []))
    print(" st.session_state:",  st.session_state)  # Debugging statement
    st.session_state["messages"].append(make_message("assistant", reply))
    with st.chat_message("assistant"):
        st.markdown(reply)
