#from app.rag.retriever import retrieve_context
from app.rag.context_builder import build_context
from app.models.llm_client import get_chat_response
from app.core.tracing import traceable

@traceable
def ask_question(question: str):

    #context = retrieve_context(question)
    context = build_context(question)

    prompt = f"""
You are a HELSB assistant.

Use SQL CONTEXT for student, loan, application, payment, and account-related questions.

Use VECTOR CONTEXT for HELSB policies, procedures, and knowledge-base questions.

If information exists in SQL CONTEXT, prioritize it over VECTOR CONTEXT.

Answer only from the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    return get_chat_response(prompt)