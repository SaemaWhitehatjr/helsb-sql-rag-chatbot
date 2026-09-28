from app.vectorstore.qdrant_client import client
from app.models.llm_client import get_embedding

from qdrant_client.models import PointStruct

text = """
HELSB allows students to defer loan repayment
under approved conditions such as further studies.
"""

embedding = get_embedding(text)

client.upsert(
    collection_name="helsb_docs",
    points=[
        PointStruct(
            id=1,
            vector=embedding,
            payload={
                "text": text
            }
        )
    ]
)

print("Vector inserted successfully")