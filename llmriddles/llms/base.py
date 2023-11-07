from typing import Callable, Dict

_LLMS: Dict[str, Callable] = {}


def register_llm(name: str, llm_ask_fn: Callable):
    _LLMS[name] = llm_ask_fn


def get_llm_fn(name: str) -> Callable:
    return _LLMS[name]
