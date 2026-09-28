from app.vectorstore.qdrant_client import client

from qdrant_client.models import (
    VectorParams,
    Distance
)

client.create_collection(
    collection_name="helsb_docs",
    vectors_config=VectorParams(
        size=3072,
        distance=Distance.COSINE
    )
)

print("Collection created successfully")
