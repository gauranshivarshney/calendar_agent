from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agent import chat_with_agent

app = FastAPI()

# For local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("user_input")
    session_id = data.get("session_id", "default")
    try:
        response = chat_with_agent(user_input, session_id)
    except Exception as e:
        print("Gemini error:", str(e))
        response = "Gemini failed"
    return {"response": response}