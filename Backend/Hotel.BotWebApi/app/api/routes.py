from fastapi import APIRouter, Body, Query
from pydantic import BaseModel
from app.agent.agente import generate_answer

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str
    conversation_id: str | None = None

@router.post("/ask")
def ask_question(payload: QuestionRequest):
    prompt = f"""Answer the following question:

Question: {payload.question}

Answer:"""
    response = generate_answer(prompt)
    return {
        "conversation_id": payload.conversation_id,
        "question": payload.question,
        "answer": response
    }

# Alternative GET endpoint using query parameters
@router.get("/ask-simple")
def ask_question_simple(
    question: str = Query(..., description="The question to ask"),
    conversation_id: str = Query(None, description="Optional conversation ID")
):
    prompt = f"""Answer the following question:

Question: {question}

Answer:"""
    response = generate_answer(prompt)
    return {
        "conversation_id": conversation_id,
        "question": question,
        "answer": response
    }