# PostgreSQL connection code will go here

import psycopg2

from app.core.config import settings


def get_connection():

    connection = psycopg2.connect(
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        database=settings.POSTGRES_DB,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD
    )

    return connection