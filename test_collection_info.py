# from app.rag.chatbot import ask_question

# response = ask_question(
#     "What students exist in the system?"
# )

# print(response)

# test_hybrid_context.py

from app.rag.context_builder import build_context

print(
    build_context(
        "What students exist in the system?"
    )
)