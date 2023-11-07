from typing import Tuple

from .question import Question
from ..llms import get_llm_fn


class QuestionExecutor:
    def __init__(self, question: Question, lang: str = 'cn', llm: str = 'chatgpt'):
        self.question = question
        self.lang = lang
        self.llm = llm

    @property
    def question_text(self):
        return self.question.texts[self.lang]

    def check(self, qs_text: str) -> Tuple[str, bool, str]:
        answer_text = get_llm_fn(self.llm)(qs_text)
        correct, explanation = self.check_answer(answer_text)
        return answer_text, correct, explanation

    def check_answer(self, answer_text: str) -> Tuple[bool, str]:
        correct, explanation = self.question.checker(self.question_text, answer_text, self.lang)
        if explanation is None:
            if correct:
                explanation = 'LLM的回答满足要求' if self.lang == 'cn' else 'Correct Answer From LLM'
            else:
                explanation = 'LLM的回答不满足要求' if self.lang == 'cn' else 'Wrong Answer From LLM'

        return correct, explanation
