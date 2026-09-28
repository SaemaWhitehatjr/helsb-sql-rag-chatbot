from app.models.llm_client import get_embedding
from app.database.qdrant import qdrant_client


query = "Can students defer loan repayment?"

query_vector = get_embedding(query)

results = qdrant_client.query_points(
    collection_name="helsb_docs",
    query=query_vector,
    limit=3
)

for result in results.points:
    print("Retrieved text:")
    print(result.payload["text"])

    print("Similarity score:")
    print(result.score)