from .question import register_question
from .utility import count_words

CN_TEXT_1 = """
第六章第一题（勇于说不），请构造一个十字以上的问题，在不提到"不"的情况下，让模型只输出"不"。

请在下面的输入框内填写你的提问并点击按钮提交。
"""

EN_TEXT_1 = """
For the first question in chapter 6, Construct a question with more than a cross so that the model only outputs "no" without saying "no".

Please enter your query below and click the submit button
"""


def _checker_1(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()

    if count_words(user_text) < 10:
        return False, "用户的问题长度应该至少10个字" if lang == 'cn' else 'Question should be no less than 10 words.'

    if lang == 'en':
        answer_text = answer_text.split()
        user_text = user_text.split()
    
    if "不" in user_text or " no " in user_text:
        return False, "问题中不能包含‘不’或‘no’" if lang == 'cn' else "The question can not contain 'no' ."
    
    if answer_text == 'no' or '不':
        return True , None 
    else:
        return False, None
    



register_question(
    {
        'cn': CN_TEXT_1,
        'en': EN_TEXT_1,
    },
    checkers=_checker_1,
    name={'cn': '6-1 勇于说不', 'en': '6-1'},
    level=6,
)
