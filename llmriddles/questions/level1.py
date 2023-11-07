from .question import register_question

def count_english_words(text: str):
    return len(text.split(' '))

def count_chinese_words(text: str):
    return len(text)

def check_if_chinese(text: str):
    return all('\u4e00' <= char <= '\u9fff' for char in text)

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
        return len(chinese_words)+len(english_words)+len(other_words)
    else:
        return len(chinese_words)+len(english_words)


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


register_question({
    'cn': CN_TEXT_1,
    'en': EN_TEXT_1,
}, _checker_1)


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


register_question({
    'cn': CN_TEXT_2,
    'en': EN_TEXT_2,
}, _checker_2)


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

register_question({
    'cn': CN_TEXT_3,
    'en': EN_TEXT_3,
}, _checker_3)


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
        return False, "大语言模型的答案应该小于100个字" if lang == 'cn' else 'Answer should be less than 20 words.'
    else:
        return True, None

register_question({
    'cn': CN_TEXT_4,
    'en': EN_TEXT_4,
}, _checker_4)


# CN_TEXT_5 = """
# 第一章第五题（回文不变），请输入一个本身不是回文串的问题，使无论正着问还是倒着问，模型的回答是一样的。

# 请在下面的输入框内填写你的问题并点击按钮提交。
# """

# EN_TEXT_5 = """
# For the fourth question in chapter 1, please enter a question that is not a palindrome string so that the model's answer is the same whether it is asked forward or backward.

# Please enter your query below and click the submit button
# """

# def _checker_5(question_text: str, answer_text: str, lang: str):
#     _ = question_text, lang
#     answer_text = answer_text.strip()

#     if count_words(question_text) > 0:
#         return False, 'Question should be one word.'
#     elif count_words(answer_text) >= 20:
#         return False, 'Answer should be less than 20 words.'
#     else:
#         return True, None

# register_question({
#     'cn': CN_TEXT_5,
#     'en': EN_TEXT_5,
# }, _checker_5)
