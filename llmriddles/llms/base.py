from typing import Callable, Dict

_LLMS: Dict[str, Callable[[str], str]] = {}


def register_llm(name: str, llm_ask_fn: Callable[[str], str]):
    _LLMS[name] = llm_ask_fn


def get_llm_fn(name: str) -> Callable[[str], str]:
    return _LLMS[name]
