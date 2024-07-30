import collections.abc
from dataclasses import dataclass
from typing import Union, Mapping, Literal, Callable, Tuple, List, Optional

LangTyping = Literal['en', 'cn']
MultiLangCheckerTyping = Callable[[str, str, str, str], Tuple[bool, Optional[str]]]
SingleLangCheckerTyping = Callable[[str, str, str], Tuple[bool, Optional[str]]]


@dataclass
class Question:
    texts: Mapping[str, str]
    checker: MultiLangCheckerTyping
    names: Mapping[str, str]
    level: int


_KNOWN_PROBLEMS = []


class Checker:

    def __init__(self, checkers, required_input_keys=None) -> None:
        self._origin_checkers = checkers
        if isinstance(checkers, collections.abc.Mapping):
            self.checker = self._integrated_checker
        else:
            self.checker = checkers

        if required_input_keys == None:
            required_input_keys = ['question_text', 'user_text', 'answer_text', 'lang']
        self.required_input_keys = required_input_keys

    def _integrated_checker(self, question_text: str, user_text: str, answer_text: str, lang: str):
        return self._origin_checkers[lang](question_text, user_text, answer_text)

    def __call__(self, inputs):
        return self.checker(*[inputs[key] for key in self.required_input_keys])


def register_question(
    text: Union[Mapping[str, str], str],
    checkers: Union[Mapping[str, SingleLangCheckerTyping], MultiLangCheckerTyping],
    name=Union[Mapping[str, str], str],
    level: int = 1,
    default_lang='cn'
):

    checker = checkers if isinstance(checkers, Checker) else Checker(checkers)

    if isinstance(text, str):
        texts = {default_lang: text}
    else:
        texts = text

    if isinstance(name, str):
        names = {default_lang: name}
    else:
        names = name

    _KNOWN_PROBLEMS.append(Question(texts, checker, names, level))


def list_ordered_questions() -> List[Question]:
    return [problem for _, problem in sorted(enumerate(_KNOWN_PROBLEMS), key=lambda x: (x[1].level, x[0]))]
