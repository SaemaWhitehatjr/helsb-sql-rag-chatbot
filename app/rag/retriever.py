from app.models.llm_client import get_embedding
from app.database.qdrant import qdrant_client
from app.core.tracing import traceable

@traceable(name="vector_retrieval")
def retrieve_context(question: str):

    query_vector = get_embedding(question)

    results = qdrant_client.query_points(
        collection_name="helsb_docs",
        query=query_vector,
        limit=3
    )

    contexts = []

    for result in results.points:
        contexts.append(
            result.payload["text"]
        )

    return "\n".join(contexts)