from app.rag.context_builder import build_context

context = build_context(
    "Can students defer loan repayment?"
)

print(context)