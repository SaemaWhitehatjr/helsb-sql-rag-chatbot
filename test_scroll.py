# test_scroll.py

from app.database.qdrant import qdrant_client

points, _ = qdrant_client.scroll(
    collection_name="helsb_docs",
    limit=10
)

for point in points:
    print(point)