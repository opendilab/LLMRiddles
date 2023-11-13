import re

from .question import register_question


from .math_tools import check_if_is_number, get_all_numbers

# CN_TEXT_1 = """
# 第四章第一题，请构造一个问题A，它的回复是不同于A的B，然后以B提问能再次得到A。

# 请在下面的输入框内填写你构造并点击按钮提交。
# """

# EN_TEXT_1 = """
# For the first question in chapter 4, please make a question A whose answer is B that is different from A, and then ask B to get A again.

# Please enter your query below and click the submit button
# """


# def _checker_1(question_text: str, user_text: str, answer_text: str, lang: str):
#     _ = question_text, lang
#     answer_text = answer_text.strip()
#     user_text = user_text.strip()
#     pass

# register_question({
#     'cn': CN_TEXT_1,
#     'en': EN_TEXT_1,
# }, _checker_1, level=4)


# CN_TEXT_2 = """
# 第四章第二题，

# 请在下面的输入框内填写你构造并点击按钮提交。
# """

# EN_TEXT_2 = """
# For the second question in chapter 4,

# Please enter your query below and click the submit button
# """


# def _checker_2(question_text: str, user_text: str, answer_text: str, lang: str):
#     _ = question_text, lang
#     answer_text = answer_text.strip()
#     user_text = user_text.strip()
#     pass

# register_question({
#     'cn': CN_TEXT_2,
#     'en': EN_TEXT_2,
# }, _checker_2, level=4)


CN_TEXT_3 = """
第四章第一题（自然之密），请输入一个大于一的正整数作为问题，使回答里包含和它刚好相差1的数。

请在下面的输入框内填写你构造并点击按钮提交。
"""

EN_TEXT_3 = """
For the first question in chapter 4, please enter a positive integer greater than one as the question so that the answer contains a number that is exactly 1 different from it.

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
