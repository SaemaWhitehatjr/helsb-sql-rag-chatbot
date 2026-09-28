# test_qdrant_connection.py

from app.database.qdrant import qdrant_client

print(qdrant_client.get_collections())