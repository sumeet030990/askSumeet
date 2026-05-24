from datetime import datetime
import streamlit as st

def empty_state():
    st.session_state["session_started"] = False
    st.session_state["session_id"] = ""
    st.session_state["user_profile"] = {"name": "", "phone": "", "email": ""}
    st.session_state["messages"] = []
  
def dummy_state():
    st.session_state["session_started"] = True
    st.session_state["session_id"] = "d02a761c-f414-43e5-ad30-ceac3626ff6f"
    st.session_state["user_profile"] = {"name": "Sumeet", "phone": "8408880505", "email": "sumeet@yopmail.com"}
    st.session_state["messages"] = []
   


def initialize_session_state():
        if "session_started" not in st.session_state:
                dummy_state()  # For development, replace with empty_state() for production
   
            
def make_message(role: str, content: str) -> dict:
    return {
        "role": role,
        "content": content,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
    }
