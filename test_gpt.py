# test_gpt.py

from app.models.llm_client import get_chat_response

response = get_chat_response(
    "What is Azure?"
)

print(response)