from functools import lru_cache

from openai import OpenAI
import os
_LLM_URL = os.environ.get('QUESTION_LLM_URL', None)
_LLM_MODEL = os.environ.get('QUESTION_LLM_MODEL', "gpt-3.5-turbo")

from .base import register_llm


@lru_cache()
def _get_openai_client(api_key):
    return OpenAI(api_key=api_key, base_url=_LLM_URL)


def ask_chatgpt(message: str, api_key: str):
    client = _get_openai_client(api_key)

    response = client.chat.completions.create(
        model=_LLM_MODEL,
        messages=[
            {"role": "user", "content": message}
        ],
    )
    return response.choices[0].message.content.strip()


register_llm('chatgpt', ask_chatgpt)
