import streamlit as st
from dotenv import load_dotenv
from view.ui import initialize_ui

load_dotenv(override=True)
st.set_page_config(page_title="Ask Sumeet", page_icon="💬", layout="centered")

def main():
    initialize_ui()

if __name__ == "__main__":
    main()
