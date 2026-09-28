# test_config.py

from app.core.config import settings

print(settings.AZURE_OPENAI_CHAT_DEPLOYMENT)
print(settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT)
print(settings.QDRANT_COLLECTION)