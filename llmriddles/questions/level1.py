from .question import register_question
from .utility import count_words, word_reverse_text
from typing import Callable
from .question import Checker
from typing import Tuple, Optional
import re

def count_english_words(text: str):
    return len(text.split(' '))


def count_chinese_words(text: str):
    return len(text)


def check_if_chinese(text: str):
    return all('\u4e00' <= char <= '\u9fff' for char in text)


CN_TEXT_1 = """
第一章第一题（初来乍到），请你构造一个问题使模型的回答是一字不差的“1+1=3”（不需要引号）。

请在下面的输入框内填写你的构造并点击按钮提交。
"""

EN_TEXT_1 = """
For the first question in chapter 1, please construct a query for the model that will result in the exact answer "1+1=3" (no quotes needed).

Please enter your query below and click the submit button
"""


def _checker_1(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()
    if answer_text == '1+1=3':
        return True, None
    else:
        return False, None


register_question(
    {
        'cn': CN_TEXT_1,
        'en': EN_TEXT_1,
    },
    checkers=_checker_1,
    name={'cn': '1-1 初来乍到', 'en': '1-1'},
)

CN_TEXT_2 = """
第一章第二题（小试牛刀），请你输入三个字（及）以内的问题，使模型的回答在30个字以上。

请在下面的输入框内填写你的问题并点击按钮提交。
"""

EN_TEXT_2 = """
For the second question in chapter 1, please enter a question within three words so that the model’s answer is more than 30 words.

Please enter your query below and click the submit button
"""


def _checker_2(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()

    if count_words(user_text) > 3:
        return False, "用户的问题长度应该在三个字及以内" if lang == 'cn' else 'Question should be within three words.'
    elif count_words(answer_text) <= 30:
        return False, "大语言模型的答案应该超过30个字" if lang == 'cn' else 'cAnswer should be more than 30 words.'
    else:
        return True, None


register_question(
    {
        'cn': CN_TEXT_2,
        'en': EN_TEXT_2,
    },
    checkers=_checker_2,
    name={'cn': '1-2 小试牛刀', 'en': '1-2'},
)

CN_TEXT_3 = """
第一章第三题（短说长话），请你输入一个字的问题，使模型的回答在100个字以上。

请在下面的输入框内填写你的问题并点击按钮提交。
"""

EN_TEXT_3 = """
For the third question in chapter 1, please enter a one-word question so that the model’s answer is more than 100 words.

Please enter your query below and click the submit button
"""


def _checker_3(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()

    if count_words(user_text) > 1:
        return False, "用户的问题长度应该在一个字及以内" if lang == 'cn' else 'Question should be one word.'
    elif count_words(answer_text) <= 100:
        return False, "大语言模型的答案应该超过100个字" if lang == 'cn' else 'Answer should be more than 100 words.'
    else:
        return True, None


register_question(
    {
        'cn': CN_TEXT_3,
        'en': EN_TEXT_3,
    },
    checkers=_checker_3,
    name={'cn': '1-3 短说长话', 'en': '1-3'}
)

CN_TEXT_4 = """
第一章第四题（短说短话），请输入一个字的问题，使模型的回答字数小于20个字。

请在下面的输入框内填写你的问题并点击按钮提交。
"""

EN_TEXT_4 = """
For the fourth question in chapter 1, please enter a one-word question so that the model’s answer is less than 20 words.

Please enter your query below and click the submit button
"""


def _checker_4(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()

    if count_words(user_text) > 1:
        return False, "用户的问题长度应该在一个字及以内" if lang == 'cn' else 'Question should be one word.'
    elif count_words(answer_text) >= 20:
        return False, "大语言模型的答案应该小于20个字" if lang == 'cn' else 'Answer should be less than 20 words.'
    else:
        return True, None


register_question(
    {
        'cn': CN_TEXT_4,
        'en': EN_TEXT_4,
    },
    checkers=_checker_4,
    name={'cn': '1-4 短说短话', 'en': '1-4'},
)

CN_TEXT_5 = """
第一章第五题（回文不变），请输入一个本身不是回文串的问题，使无论正着问还是倒着问，模型的回答是一样的。

请在下面的输入框内填写你的问题并点击按钮提交。
"""

EN_TEXT_5 = """
For the fifth question in chapter 1, please enter a question that is not a palindrome string so that the model's answer is the same whether it is asked forward or backward.

Please enter your query below and click the submit button
"""

def _checker_5(question_text: str, user_text: str, answer_text: str, lang: str, llm_callback: Callable[[str], str]):
    answer_text = answer_text.strip()
    user_text = user_text.strip()
    reversed_user_text = word_reverse_text(user_text, lang)
    second_answer_text = llm_callback(reversed_user_text)

    if user_text == reversed_user_text:
        return False, "用户的问题不能是回文串" if lang == 'cn' else 'Question should not be a palindrome string.'

    if second_answer_text != answer_text:
        return False, f"正着问和倒着问时，模型的回答应该是一样的\n 问题：{user_text}\n 正着问回答：{answer_text}\n 反着问回答：{second_answer_text}" if lang == 'cn' else f'The model\'s answer should be the same when asked forward or backward.\n Question: {user_text}\n Forward-Asking answer: {answer_text}\n Backward-Asking answer: {second_answer_text}'
    return True, None

register_question(
    {
        'cn': CN_TEXT_5,
        'en': EN_TEXT_5,
    }, 
    checkers=Checker(_checker_5, required_input_keys=['question_text', 'user_text', 'answer_text', 'lang', 'llm_callback']), 
    name={'cn': '1-5 回文不变', 'en': '1-5'},
    level=1,
)

CN_TEXT_6 = """
第一章第六题（无中生狗），请提一个不包含“狗”这个字的问题，但是回答中至少出现3次“狗”这个字。

请在下面的输入框内填写你的问题并点击按钮提交。
"""

EN_TEXT_6 = """
For the sixth question in chapter 1, please ask a question that does not contain the word "dog", but the answer contains the word "dog" at least three times.

Please enter your query below and click the submit button
"""


def _cn_checker_6(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    if '狗' in user_text:
        return False, '问题不得包含“狗”字'

    dog_count = len(re.findall('狗', answer_text))
    if dog_count >= 3:
        return True, f'“狗”字的出现次数为{dog_count}次'
    else:
        return False, f'“狗”字的出现次数为{dog_count}次，未达到3次'

def _en_checker_6(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    q_words = re.findall(r'\w+', user_text.lower())
    if any(word in {'dog', 'dogs'} for word in q_words):
        return False, 'The question must not contain the word "dog" or "dogs"'

    a_words = re.findall(r'\w+', answer_text.lower())
    a_dog_count = sum(1 if word in {'dog', 'dogs'} else 0 for word in a_words)
    if a_dog_count >= 3:
        return True, f'The word "dog" (or "dogs") appears {a_dog_count} times.'
    else:
        return False, f'The word "dog" (or "dogs") appears {a_dog_count} times, ' \
                      f'which is less than 3 times.'

register_question(
    {
        'cn': CN_TEXT_6,
        'en': EN_TEXT_6,
    },
    checkers={
        'cn': _cn_checker_6,
        'en': _en_checker_6,
    },
    name={'cn': '1-6 无中生狗', 'en': '1-6'},
    level=1,
)