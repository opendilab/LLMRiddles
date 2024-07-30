from .question import register_question
from .utility import count_words
import re
import string

CN_TEXT_1 = """
第六章第一题（勇于说不），请构造一个十字以上的问题，在不提到"不"的情况下，让模型只输出"不"。

请在下面的输入框内填写你的提问并点击按钮提交。
"""

EN_TEXT_1 = """
For the first question in chapter 6, Construct a question with more than a cross so that the model only outputs "no" without saying "no".

Please enter your query below and click the submit button
"""


def _checker_1(question_text: str, user_text: str, answer_text: str, lang: str) -> tuple[bool, str | None]:
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()

    if count_words(user_text) < 10:
        return False, "用户的问题长度应该至少10个字" if lang == 'cn' else 'Question should be no less than 10 words.'

    if lang == 'en':
        answer_text = answer_text.split()
        user_text = user_text.split()

    chinese_punctuation = {'，', '。', '、', '；', '：', '“', '”', '‘', '’', '（', '）', '《', '》', '……', '——', '～'}
    all_punctuation = set(string.punctuation).union(chinese_punctuation)

    matches = re.finditer(r'no', user_text, re.IGNORECASE)

    for match in matches:

        char_before = user_text[match.start() - 1] if match.start() > 0 else ''
        char_after = user_text[match.end()] if match.end() < len(user_text) else ''

        if not (char_before.isalnum() or char_after.isalnum()):
            return False, "问题中不能包含‘不’或‘no’" if lang == 'cn' else "The question cannot contain 'no'."

        if (char_before in all_punctuation or re.search('[\u4e00-\u9fff]', char_before)) and \
           (char_after in all_punctuation or re.search('[\u4e00-\u9fff]', char_after)):
            return False, "问题中不能包含‘不’或‘no’" if lang == 'cn' else "The question cannot contain 'no'."

    if lang == 'cn' and answer_text == "不":
        return True, None
    elif lang == 'en' and answer_text == "no":
        return True, None
    else:
        return False, None


register_question(
    {
        'cn': CN_TEXT_1,
        'en': EN_TEXT_1,
    },
    checkers=_checker_1,
    name={
        'cn': '6-1 勇于说不',
        'en': '6-1'
    },
    level=6,
)
