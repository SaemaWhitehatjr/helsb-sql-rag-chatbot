import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "HELSB SQL RAG Chatbot")

    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

    AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv(
        "AZURE_OPENAI_CHAT_DEPLOYMENT"
    )

    AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv(
        "AZURE_OPENAI_EMBEDDING_DEPLOYMENT"
    )

    QDRANT_URL = os.getenv(
        "QDRANT_URL",
        "http://localhost:6333"
    )

    QDRANT_COLLECTION = os.getenv(
        "QDRANT_COLLECTION",
        "helsb_documents"
    )

    POSTGRES_HOST = os.getenv(
        "POSTGRES_HOST",
        "localhost"
    )

    POSTGRES_PORT = os.getenv(
        "POSTGRES_PORT",
        "5432"
    )

    POSTGRES_DB = os.getenv(
        "POSTGRES_DB"
    )

    POSTGRES_USER = os.getenv(
        "POSTGRES_USER"
    )

    POSTGRES_PASSWORD = os.getenv(
        "POSTGRES_PASSWORD"
    )


settings = Settings()