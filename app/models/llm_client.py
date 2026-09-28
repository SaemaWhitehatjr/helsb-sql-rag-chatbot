from openai import AzureOpenAI

from app.core.config import settings


client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_API_KEY,
    api_version="2024-12-01-preview",
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
)


def get_embedding(text: str):

    response = client.embeddings.create(
        model=settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
        input=text
    )

    return response.data[0].embedding

def get_chat_response(prompt: str):

    response = client.chat.completions.create(
        model=settings.AZURE_OPENAI_CHAT_DEPLOYMENT,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content