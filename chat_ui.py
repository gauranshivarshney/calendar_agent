import streamlit as st
import requests

st.set_page_config(page_title="AI Scheduler", page_icon="📅")

st.title("📅 Appointment Booking Assistant")
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", key="input")
if user_input:
    try:
        response = requests.post("http://localhost:8000/chat", json={"user_input": user_input})
        if response.status_code == 200:
            ai_message = response.json().get("response", "No reply")
        else:
            ai_message = f"Server error: {response.status_code}"
    except Exception as e:
        ai_message = f"Could not connect"
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("AI", response.json()["response"]))

for sender, message in st.session_state.messages:
    st.markdown(f"**{sender}:** {message}")