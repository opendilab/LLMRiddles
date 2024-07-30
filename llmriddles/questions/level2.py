import re
from typing import Optional, Tuple

import sympy

from .question import register_question
from .math_tools import get_all_numbers

CN_TEXT_1 = """
第二章第一题（质数长度），你需要提出一个字数是质数的问题，使回答的长度刚好是它的下一个质数。
"""
EN_TEXT_1 = """
For the first question in chapter 2, You need to come up with a question that has a prime number of words, so the answer's length is exactly the next prime number.
"""


def _is_prime(v):
    return sympy.isprime(v)


def _next_prime(v):
    while v:
        v += 1
        if _is_prime(v):
            return v


def _cn_checker_1(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    qs_length = len(user_text.strip())
    if not _is_prime(qs_length):
        return False, f'问题长度为{qs_length}，非质数'

    answer_value = len(answer_text)
    next_prime = _next_prime(qs_length)
    if answer_value != next_prime:
        return False, f'下一个质数为{next_prime}，但回答长度为{answer_value}'

    return True, None


def _en_words(text: str):
    return len(re.findall(r'\w+', text))


def _en_checker_1(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    qs_length = _en_words(user_text.strip())
    if not _is_prime(qs_length):
        return False, f'The question has a length of {qs_length}, which is not a prime number'

    answer_value = _en_words(answer_text)
    next_prime = _next_prime(qs_length)
    if answer_value != next_prime:
        return False, f'The next prime number is {next_prime}, but the answer\'s length is {answer_value}'

    return True, None


register_question(
    {
        'cn': CN_TEXT_1,
        'en': EN_TEXT_1,
    },
    checkers={
        'cn': _cn_checker_1,
        'en': _en_checker_1,
    },
    name={
        'cn': '2-1 质数长度',
        'en': '2-1'
    },
    level=2
)

CN_TEXT_2 = """
第二章第二题（越说越大），请输入一个大于一的正整数作为问题，使回答里包含至少比它大一千的数。
"""
EN_TEXT_2 = """
For the second question in chapter 2, Please enter a positive integer greater than one as a question, so that the answer contains a number that is at least one thousand more than it.
"""


def _cn_checker_2(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    try:
        value = int(user_text.strip())
        if value <= 1:
            raise ValueError
    except (TypeError, ValueError):
        return False, f'输入内容{user_text!r}，并非一个大于1的正整数'

    for value_item in get_all_numbers(answer_text):
        if value_item >= value + 1000:
            return True, f'检测到输出中数字{value_item}，满足要求'

    return False, f'未在输出中检测到不少于{value + 1000}的数字'


def _en_checker_2(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    try:
        value = int(user_text.strip())
        if value <= 1:
            raise ValueError
    except (TypeError, ValueError):
        return False, f'You entered {user_text!r}, which is not a positive integer greater than 1'

    for value_item in get_all_numbers(answer_text):
        if value_item >= value + 1000:
            return True, f'Detected the number {value_item} in the output, which meets the requirement'

    return False, f'Did not detect a number of at least {value + 1000} in the output'


register_question(
    {
        'cn': CN_TEXT_2,
        'en': EN_TEXT_2,
    },
    checkers={
        'cn': _cn_checker_2,
        'en': _en_checker_2,
    },
    name={
        'cn': '2-2 越说越大',
        'en': '2-2'
    },
    level=2
)

CN_TEXT_3 = """
第二章第三题（越说越小），请输入一个大于一的正整数作为问题，使回答里包含至少10个不同的至少比它小一千的自然数。
"""
EN_TEXT_3 = """
For the third question in chapter 2, Please enter a positive integer greater than one as a question, so that the answer contains at least 10 different natural numbers, each of them at least 1000 less than the question.
"""


def _cn_checker_3(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    try:
        value = int(user_text.strip())
        if value <= 1:
            raise ValueError
    except (TypeError, ValueError):
        return False, f'输入内容{user_text!r}，并非一个大于1的正整数'

    collected_values = []
    for value_item in get_all_numbers(answer_text):
        if value_item <= value - 1000:
            collected_values.append(value_item)

    collected_values = sorted(set(collected_values))
    if len(collected_values) >= 10:
        return True, f'检测到{len(collected_values)}个不大于{value - 1000}的数字：{collected_values!r}'
    else:
        return False, f'检测到{len(collected_values)}个不大于{value - 1000}的数字,未达到10个：{collected_values!r}'


def _en_checker_3(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    try:
        value = int(user_text.strip())
        if value <= 1:
            raise ValueError
    except (TypeError, ValueError):
        return False, f'You entered {user_text!r}, which is not a positive integer greater than 1'

    collected_values = []
    for value_item in get_all_numbers(answer_text):
        if value_item <= value - 1000:
            collected_values.append(value_item)

    collected_values = sorted(set(collected_values))
    if len(collected_values) >= 10:
        return True, f'Detected {len(collected_values)} numbers not greater than {value - 1000}: {collected_values!r}'
    else:
        return False, f'Detected {len(collected_values)} numbers not greater than {value - 1000}, ' \
                      f'but it doesn\'t reach 10: {collected_values!r}'


register_question(
    {
        'cn': CN_TEXT_3,
        'en': EN_TEXT_3,
    },
    checkers={
        'cn': _cn_checker_3,
        'en': _en_checker_3,
    },
    name={
        'cn': '2-3 越说越小',
        'en': '2-3'
    },
    level=2,
)

CN_TEXT_4 = """
第二章第四题（警世名言），请在不提及1,4,5这三个字符的情况下让模型回答114514，不要有多余的字符。
"""
EN_TEXT_4 = """
For the fourth question in chapter 2, Please make the model answer "114514" without mentioning the characters 1, 4, and 5, and without any extra characters.
"""


def _cn_checker_4(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    if "1" in user_text or "4" in user_text or "5" in user_text:
        return False, '请不要在提问中出现1、4、5三个数字'

    return answer_text.strip() == '114514', None


def _en_checker_4(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    if "1" in user_text or "4" in user_text or "5" in user_text:
        return False, 'Please don\'t include the numbers 1, 4, and 5 in the question'

    return answer_text.strip() == '114514', None


register_question(
    {
        'cn': CN_TEXT_4,
        'en': EN_TEXT_4,
    },
    checkers={
        'cn': _cn_checker_4,
        'en': _en_checker_4,
    },
    name={
        'cn': '2-4 警世名言',
        'en': '2-4'
    },
    level=2,
)

CN_TEXT_5 = """
第二章第五题（开平方数），请输入一个大于一的平方数作为问题，使回答里包含它的平方根对应的数。
"""
EN_TEXT_5 = """
For the fifth question in chapter 2, Please provide a square number greater than one as the question, and the answer should include the number corresponding to its square root.
"""


def _cn_checker_5(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    try:
        value = int(user_text.strip())
        if value <= 1:
            raise ValueError
        if int(value ** 0.5) ** 2 != value:
            raise ValueError
    except (TypeError, ValueError):
        return False, f'输入内容{user_text!r}，并非一个大于1的平方数'

    sq = int(value ** 0.5)
    for value_item in get_all_numbers(answer_text):
        if value_item == sq:
            return True, f'检测到平方根数{sq}'
    else:
        return False, f'未检测到平方根数{sq}'


def _en_checker_5(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    try:
        value = int(user_text.strip())
        if value <= 1:
            raise ValueError
        if int(value ** 0.5) ** 2 != value:
            raise ValueError
    except (TypeError, ValueError):
        return False, f'The input, {user_text!r}, is not a square number greater than 1'

    sq = int(value ** 0.5)
    for value_item in get_all_numbers(answer_text):
        if value_item == sq:
            return True, f'Detected square root: {sq}'
    else:
        return False, f'Square root {sq} not detected'


register_question(
    {
        'cn': CN_TEXT_5,
        'en': EN_TEXT_5,
    },
    checkers={
        'cn': _cn_checker_5,
        'en': _en_checker_5,
    },
    name={
        'cn': '2-5 开平方数',
        'en': '2-5'
    },
    level=2,
)

CN_TEXT_6 = """
第二章第六题（得寸进狗），请提一个不包含“狗”这个字的10个字以内的问题，使回答中“狗”这个字出现的次数至少是问题字数的2倍。
"""
EN_TEXT_6 = """
For the sixth question in chapter 2, Please ask a question in under 10 words without the word "dog" and ensure that the word "dog" appears at least twice in the answer for each word in the question.
"""


def _cn_checker_6(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    if len(user_text) > 10:
        return False, '问题不得超过10个字'
    if '狗' in user_text:
        return False, '问题不得包含“狗”字'

    dog_count = len(re.findall('狗', answer_text))
    if dog_count >= len(user_text) * 2:
        return True, f'“狗”字的出现次数为{dog_count}次'
    else:
        return False, f'“狗”字的出现次数为{dog_count}次，未达到{len(user_text) * 2}次'


def _en_checker_6(question_text: str, user_text: str, answer_text: str) -> Tuple[bool, Optional[str]]:
    q_words = re.findall(r'\w+', user_text.lower())
    if len(q_words) > 10:
        return False, 'The question must not exceed 10 words'
    if any(word in {'dog', 'dogs'} for word in q_words):
        return False, 'The question must not contain the word "dog" or "dogs"'

    a_words = re.findall(r'\w+', answer_text.lower())
    a_dog_count = sum(1 if word in {'dog', 'dogs'} else 0 for word in a_words)
    if a_dog_count >= len(q_words) * 2:
        return True, f'The word "dog" (or "dogs") appears {a_dog_count} times.'
    else:
        return False, f'The word "dog" (or "dogs") appears {a_dog_count} times, ' \
                      f'which is less than {len(q_words) * 2} times.'


register_question(
    {
        'cn': CN_TEXT_6,
        'en': EN_TEXT_6,
    },
    checkers={
        'cn': _cn_checker_6,
        'en': _en_checker_6,
    },
    name={
        'cn': '2-6 得寸进狗',
        'en': '2-6'
    },
    level=2
)
