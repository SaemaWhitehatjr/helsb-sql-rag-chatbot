# test_methods.py

from app.database.qdrant import qdrant_client

print([m for m in dir(qdrant_client) if "query" in m.lower()])