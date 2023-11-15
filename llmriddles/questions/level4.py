import re

from .question import register_question
from .question import Checker
from typing import Callable
from .utility import count_words, word_reverse_text

from .math_tools import check_if_is_number, get_all_numbers

CN_TEXT_1 = """
第四章第一题（循环往复），请构造一个问题A，它的回复是不同于A的B，然后以B提问能再次得到A。

请在下面的输入框内填写你构造并点击按钮提交。
"""

EN_TEXT_1 = """
For the first question in chapter 4, please make a question A whose answer is B that is different from A, and then ask B to get A again.

Please enter your query below and click the submit button
"""

def _checker_1(question_text: str, user_text: str, answer_text: str, lang: str, llm_callback: Callable[[str], str]):
    answer_text = answer_text.strip()
    user_text = user_text.strip()
    second_answer_text = llm_callback(answer_text)

    if second_answer_text != user_text:
        return False, f"B产生的回答和原问题A不一致:\n A: {user_text}\n B: {answer_text}\n Answer from B: {second_answer_text}" if lang == 'cn' else f'The answer from B is not the same as the original question A:\n A: {user_text}\n B: {answer_text}\n Answer from B: {second_answer_text}'
    
    return True, None
    
register_question(
    {
        'cn': CN_TEXT_1,
        'en': EN_TEXT_1,
    },
    checkers=Checker(_checker_1, required_input_keys=['question_text', 'user_text', 'answer_text', 'lang', 'llm_callback']), 
    name={'cn': '4-1 循环往复', 'en': '4-1'},
    level=4,
)

CN_TEXT_2 = """
第四章第二题（惜字如金），本题可能没有答案，你可以自由的先去做其他的题。请输入一个字的问题，使模型的回答在16个字以内。

请在下面的输入框内填写你构造并点击按钮提交。
"""

EN_TEXT_2 = """
For the second question in chapter 4, please enter a question of one word so that the model's answer is within 16 words (The Chinese version of this problem may not have a correct answer, but the English version might).

Please enter your query below and click the submit button
"""


def _checker_2(question_text: str, user_text: str, answer_text: str, lang: str):
    answer_text = answer_text.strip()
    user_text = user_text.strip()
    if count_words(user_text) > 1:
        return False, "用户的问题长度应该在一个字以内" if lang == 'cn' else 'Question should be within one word.'

    if count_words(answer_text) > 16:
        return False, "大语言模型的答案应该在16个字以内" if lang == 'cn' else 'Answer should be within 16 words.'
    else:
        return True, None

register_question(
    {
        'cn': CN_TEXT_2,
        'en': EN_TEXT_2,
    },
    checkers=_checker_2,
    name={'cn': '4-2 惜字如金', 'en': '4-2'},
    level=4,
)


CN_TEXT_3 = """
第四章第三题（自然之密），请输入一个大于一的正整数作为问题，使回答里包含和它刚好相差1的数。

请在下面的输入框内填写你构造并点击按钮提交。
"""

EN_TEXT_3 = """
For the third question in chapter 4, please enter a positive integer greater than one as the question so that the answer contains a number that is exactly 1 different from it.

Please enter your query below and click the submit button
"""


def _checker_3(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()
    if not check_if_is_number(user_text):
        return False, "问题应该是一个正整数" if lang == 'cn' else 'Question should be a positive integer.'
    elif int(user_text) == 1:
        return False, "问题应该是一个大于1的正整数" if lang == 'cn' else 'Question should be a positive integer greater than 1.'
    elif int(user_text) - 1 not in get_all_numbers(answer_text) and int(
            user_text) + 1 not in get_all_numbers(answer_text):
        return False, "回答中应该包含一个与问题相差1的数字" if lang == 'cn' else 'Answer should contain a number that is exactly 1 different from the question.'
    else:
        return True, None


register_question(
    {
        'cn': CN_TEXT_3,
        'en': EN_TEXT_3,
    },
    checkers=_checker_3,
    name={'cn': '4-3 自然之密', 'en': '4-3'},
    level=4,
)
