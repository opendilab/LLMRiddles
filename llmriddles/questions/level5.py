from .question import register_question
from .utility import count_words

CN_TEXT_1 = """
第五章第一题（口是心非），请构造一个不少于十个字的问题，使得回答中不包含问题中的任意字符。

请在下面的输入框内填写你的提问并点击按钮提交。
"""

EN_TEXT_1 = """
For the first question in chapter 5, Please construct a question of no less than ten words so that the answer does not contain any of the characters in the question.

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
        return True, None
    else:
        return False, None


register_question(
    {
        'cn': CN_TEXT_1,
        'en': EN_TEXT_1,
    },
    checkers=_checker_1,
    name={'cn': '5-1 口是心非', 'en': '5-1'},
    level=5,
)
