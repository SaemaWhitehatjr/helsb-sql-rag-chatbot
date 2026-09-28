from app.rag.retriever import retrieve_context

context = retrieve_context(
    "Can students defer loan repayment?"
)

print(context)