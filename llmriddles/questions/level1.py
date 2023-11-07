from .question import register_question

CN_TEXT = """
欢迎来玩LLM Riddles!

你将通过本游戏对语言大模型产生更深刻的理解。

在本游戏中，你需要构造一个提给一个语言大模型的问题，使得它回复的答案符合要求。

作为第一个题目，请你构造一个问题使模型的回答是一字不差的“1+1=3”（不需要引号）。

请在下面的输入框内填写你构造并点击按钮提交。
"""

EN_TEXT = """
Welcome to LLM Riddles!

In this game, you'll gain a deeper understanding of language models.

Your challenge is to create a question to ask a language model in a way that the answer it provides meets specific criteria.

For the first question, please construct a query for the model that will result in the exact answer "1+1=3" (no quotes needed).

Please enter your query below and click the submit button
"""


def _checker(question_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    if answer_text == '1+1=3':
        return True, None
    else:
        return False, None


register_question({
    'cn': CN_TEXT,
    'en': EN_TEXT,
}, _checker)
