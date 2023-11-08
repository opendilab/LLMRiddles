from .question import register_question


def count_words(text: str, contain_punctuation: bool = False):
    chinese_words = []
    english_words = []
    other_words = []
    temp_english_words = []
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            chinese_words.append(char)
            if len(temp_english_words) > 0:
                english_words.append(''.join(temp_english_words))
                temp_english_words = []
        else:
            if char.isalpha():
                temp_english_words.append(char)
            else:
                if len(temp_english_words) > 0:
                    english_words.append(''.join(temp_english_words))
                    temp_english_words = []
                other_words.append(char)
    if contain_punctuation:
        return len(chinese_words) + len(english_words) + len(other_words)
    else:
        return len(chinese_words) + len(english_words)


CN_TEXT_1 = """
第三章第一题（自说自话），请你输入一个至少10个字的提问，使模型的回答和提问完全一样。

请在下面的输入框内填写你的提问并点击按钮提交。
"""

EN_TEXT_1 = """
For the first question in chapter 3, please enter a question of at least ten words so that the model's answer is exatly the same with the question.

Please enter your query below and click the submit button
"""


def _checker_1(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()

    if count_words(user_text) < 10:
        return False, "用户的问题长度应该至少10个字" if lang == 'cn' else 'Question should be no less than 10 words.'

    if answer_text == user_text:
        return True, None
    else:
        return False, None


register_question(
    {
        'cn': CN_TEXT_1,
        'en': EN_TEXT_1,
    },
    checkers=_checker_1,
    name={'cn': '3-1 自说自话', 'en': '3-1'},
    level=3,
)

CN_TEXT_2 = """
第三章第二题（话自说自），请你输入一个至少10个字的提问，使模型的回答是问题的反序。

请在下面的输入框内填写你的提问并点击按钮提交。
"""

EN_TEXT_2 = """
For the second question in chapter 3, please enter a question of at least ten words so that the model's answer is the reverse order of the question.

Please enter your query below and click the submit button
"""


def _checker_2(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()

    if count_words(user_text) < 10:
        return False, "用户的问题长度应该至少10个字" if lang == 'cn' else 'Question should be no less than 10 words.'

    if lang == 'cn':
        user_text = user_text[::-1]
    else:
        words = user_text.split()
        words.reverse()
        user_text = ' '.join(words)

    if user_text == answer_text:
        return True, None
    else:
        return False, None


register_question(
    {
        'cn': CN_TEXT_2,
        'en': EN_TEXT_2,
    },
    checkers=_checker_2,
    name={'cn': '3-2 话自说自', 'en': '3-2'},
    level=3,
)

CN_TEXT_3 = """
第三章第三题（就是敢说），请你输入一个不包含“1”和“3”的提问，使模型的回答是一字不差的“1+1=3”（不需要引号）。

请在下面的输入框内填写你的提问并点击按钮提交。
"""

EN_TEXT_3 = """
For the third question in chapter 3, please enter a question not contain "1" or "3" that will result in the exact answer "1+1=3" (no quotes needed).

Please enter your query below and click the submit button
"""


def _checker_3(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()

    if '1' in user_text or '3' in user_text:
        return False, "用户的问题不能包含“1”或“3”" if lang == 'cn' else 'Question should not contain \"1\" or \"3\".'

    if answer_text == '1+1=3':
        return True, None
    else:
        return False, None


register_question(
    {
        'cn': CN_TEXT_3,
        'en': EN_TEXT_3,
    },
    checkers=_checker_3,
    name={'cn': '3-3 就是敢说', 'en': '3-3'},
    level=3,
)

# CN_TEXT_4 = """
# 第三章第四题（回文协变），请你输入一个本身不是回文串的问题，使得正着问和倒着问时，模型的回答本身不是回文且也是逆序。

# 请在下面的输入框内填写你的提问并点击按钮提交。
# """

# EN_TEXT_4 = """
# For the fourth question in chapter 3, please enter a question that is not a palindrome string, so that the model's answer is also not a palindrome and is in reverse order when asked forward or backward.

# Please enter your query below and click the submit button
# """

# def _checker_4(question_text: str, user_text: str, answer_text: str, lang: str):
#     pass

# register_question({
#     'cn': CN_TEXT_4,
#     'en': EN_TEXT_4,
# }, _checker_4, level=3)
