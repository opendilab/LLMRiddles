from typing import Tuple

from .question import Question
from ..llms import get_llm_fn


class QuestionExecutor:
    def __init__(self, question: Question, lang: str = 'cn', llm: str = 'chatgpt', llm_cfgs=None):
        self.question = question
        self.lang = lang
        self.llm = llm
        self.llm_cfgs = dict(llm_cfgs or {})

    @property
    def question_text(self):
        return self.question.texts[self.lang]

    @property
    def question_name(self):
        return self.question.names[self.lang]
    
    def llm_answer(self, qs_text: str) -> str:
        return get_llm_fn(self.llm)(qs_text, **self.llm_cfgs)

    def check(self, qs_text: str) -> Tuple[str, bool, str]:
        answer_text = self.llm_answer(qs_text)
        correct, explanation = self.check_answer(qs_text, answer_text)
        return answer_text, correct, explanation

    def check_answer(self, user_text: str, answer_text: str) -> Tuple[bool, str]:
        inputs = {
            'question_text': self.question_text,
            'user_text': user_text,
            'answer_text': answer_text,
            'lang': self.lang,
            'llm_callback': self.llm_answer,
            # this list can be extended if needed in the future 
        }
        correct, explanation = self.question.checker(inputs)
        if explanation is None:
            if correct:
                explanation = 'LLM的回答满足要求' if self.lang == 'cn' else 'Correct Answer From LLM'
            else:
                explanation = 'LLM的回答不满足要求' if self.lang == 'cn' else 'Wrong Answer From LLM'

        return correct, explanation
