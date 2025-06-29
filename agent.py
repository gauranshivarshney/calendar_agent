from dotenv import load_dotenv
load_dotenv()
from langgraph.graph import StateGraph
from langgraph.pregel import Pregel
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from datetime import datetime, timedelta
from calendar_utils import check_availability, book_slot, extract_time_range
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

# Define LangGraph workflow
def chat_with_agent(user_input, session_id):
    # Step 1: Understand intent & time
    try:
        response = model.generate_content(user_input, generation_config={"temperature": 0.7})
        return response.text
    except Exception as e:
        print("Gemini error:", str(e))
        return "Hmm"
