from fastapi import FastAPI
from app.models.chat_request import ChatRequest
from app.rag.chatbot import ask_question

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "HELSB SQL-RAG Chatbot is running"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    answer = ask_question(request.question)

    return {
        "question": request.question,
        "answer": answer
    }

@app.get("/health")
def health():

    return {
        "status": "healthy",
        
        "service": "HELSB SQL-RAG Chatbot"
    }