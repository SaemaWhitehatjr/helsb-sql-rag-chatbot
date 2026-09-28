from app.core.tracing import traceable
from app.rag.retriever import retrieve_context
from app.rag.sql_service import get_student_context

@traceable(name="build_hybrid_context")
def build_context(question: str):

    vector_context = retrieve_context(question)

    sql_context = get_student_context()

    return f"""
VECTOR CONTEXT:
{vector_context}

SQL CONTEXT:
{sql_context}
"""