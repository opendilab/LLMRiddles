from functools import lru_cache

from .base import register_llm
from .llm_client import LLMFlaskClient


@lru_cache()
def _get_mistral_7b_instruct_server(host: str, port: int):
    from .llm_server import LLMInstance, create_app
    core = LLMInstance('Mistral-7B-Instruct-v0.1')
    app = create_app(core)
    app.run(host=host, port=port)


def ask_mistral_7b_instruct(message: str, **kwargs):
    host, port = '0.0.0.0', 8001
    _get_mistral_7b_instruct_server(host, port)
    client = LLMFlaskClient(host, port)
    return client.run(message).strip()


register_llm('mistral-7b', ask_mistral_7b_instruct)
