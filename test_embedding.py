from app.models.llm_client import get_embedding

embedding = get_embedding(
    "HELSB Loan Policy"
)

print(len(embedding))