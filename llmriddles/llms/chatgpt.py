import os
from functools import lru_cache

import openai

from .base import register_llm


@lru_cache()
def _setup_openai():
    current_path = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(current_path)
    if 'OPENAI_KEY' in os.environ:
        openai.api_key = os.environ['OPENAI_KEY']
    else:
        openai.api_key_path = f'{parent_dir}/.key'


def ask_chatgpt(message: str):
    _setup_openai()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ],
    )
    return response["choices"][0]["message"]["content"].strip()


register_llm('chatgpt', ask_chatgpt)
