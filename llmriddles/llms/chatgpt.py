from functools import lru_cache

from openai import OpenAI

from .base import register_llm


@lru_cache()
def _get_openai_client(api_key):
    return OpenAI(api_key=api_key)


def ask_chatgpt(message: str, api_key: str):
    client = _get_openai_client(api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": message
        }],
    )
    return response.choices[0].message.content.strip()


register_llm('chatgpt', ask_chatgpt)
