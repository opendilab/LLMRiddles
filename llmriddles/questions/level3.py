from .question import register_question

CN_TEXT = """
第3题 短说长话

请输入一个字的问题，使模型的回答在100个字以上。

请在下面的输入框内填写你构造并点击按钮提交。
"""

EN_TEXT = """
Level 3. Less for more

Please enter a one-word question so that the model's answer is 100 words or more.

Please enter your query below and click the submit button
"""


def _checker(question_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    if len(question_text) == 1 and len(answer_text) >= 100:
        return True, None
    else:
        return False, None


register_question({
    'cn': CN_TEXT,
    'en': EN_TEXT,
}, _checker)
