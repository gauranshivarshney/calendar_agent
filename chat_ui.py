import streamlit as st
import requests
import os

st.set_page_config(page_title="AI Scheduler", page_icon="📅")

st.title("📅 Appointment Booking Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Use backend API URL from env or fallback to localhost
API_URL = os.getenv("API_URL", "http://localhost:8000")

user_input = st.text_input("You:", key="input")

if user_input:
    try:
        response = requests.post(f"{API_URL}/chat", json={"user_input": user_input})
        if response.status_code == 200:
            ai_message = response.json().get("response", "No reply")
        else:
            ai_message = f"Server error: {response.status_code}"
    except Exception as e:
        ai_message = "Could not connect to backend."

    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("AI", ai_message))

for sender, message in st.session_state.messages:
    st.markdown(f"**{sender}:** {message}")
