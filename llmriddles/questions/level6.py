from .question import register_question
from .utility import count_words

CN_TEXT_1 = """
第六章第一题（口非心是），请构造一个不少于十个字的问题，使得回答在不重复问题的句子的情况下，包含问题中的所有字符。

请在下面的输入框内填写你的提问并点击按钮提交。
"""

EN_TEXT_1 = """
For the first question in chapter 6, Please construct a question of at least ten words so that the answer contains all the characters in the question without repeating the sentence of the question.

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
    
    if not any(each in answer_text for each in user_text):
        return False, "回答中必须包含问题中的所有字符" if lang == 'cn' else 'The answer must contain all the characters in the question.'
    
    if user_text in answer_text:
        return False, "回答中不能直接复制整个问题句子"
    else:
        return True, None
    



register_question(
    {
        'cn': CN_TEXT_1,
        'en': EN_TEXT_1,
    },
    checkers=_checker_1,
    name={'cn': '6-1 口非心是', 'en': '6-1'},
    level=6,
)
