import os
import uuid

import gradio as gr

from llmriddles.questions import QuestionExecutor
from llmriddles.questions import list_ordered_questions

_QUESTION_IDS = {}
_QUESTIONS = list_ordered_questions()
_LANG = os.environ.get('QUESTION_LANG', 'cn')
_LLM = os.environ.get('QUESTION_LLM', 'chatgpt')

if _LANG == "cn":
    requirement_ph = "点击\"下一题\"开始游戏"
    requirement_label = "游戏须知"
    question_ph = "你对大语言模型的提问"
    question_label = "提问栏"
    answer_ph = "大语言模型的回答"
    answer_label = "回答栏"
    submit_label = "提交"
    next_label = "下一题"
    api_ph = "你个人的大语言模型 API Key (例如：ChatGPT)"
    api_label = "API key"
    predict_label = "结果正确性"
    explanation_label = "结果解释"
    game_cleared_label = "祝贺！你已成功通关！"
    correct_label = "正确"
    wrong_label = "错误"
    api_error_info = "请在提交问题之前先输入你的 API Key"
    try_again_label = "再玩一次"
elif _LANG == "en":
    requirement_ph = 'Click \'Next\' to Start'
    requirement_label = "Requirements"
    question_ph = "Your Question for LLM"
    question_label = "Question"
    answer_ph = "Answer From LLM"
    answer_label = "Answer"
    submit_label = "Submit"
    next_label = "Next"
    api_ph = "Your API Key (e.g. ChatGPT)"
    api_label = "API key"
    predict_label = "Correctness"
    explanation_label = "Explanation"
    game_cleared_label = "Congratulations!"
    correct_label = "Correct"
    wrong_label = "Wrong"
    api_error_info = "Please Enter API Key Before Submitting Question."
    try_again_label = "Try Again"
else:
    raise KeyError("invalid _LANG: {}".format(_LANG))


def _need_api_key():
    return _LLM == 'chatgpt'


def _get_api_key_cfgs(api_key):
    if _LLM == 'chatgpt':
        return {'api_key': api_key}
    else:
        return {}


if __name__ == '__main__':
    with gr.Blocks(theme='ParityError/Interstellar') as demo:
        with gr.Row():
            with gr.Column():
                gr_requirement = gr.TextArea(placeholder=requirement_ph, label=requirement_label)
                gr_question = gr.TextArea(placeholder=question_ph, label=question_label)
                gr_answer = gr.TextArea(placeholder=answer_ph, label=answer_label)
                gr_submit = gr.Button(submit_label, interactive=False)

            with gr.Column():
                gr_api_key = gr.Text(placeholder=api_ph, label=api_label, type='password',
                                     visible=_need_api_key())
                gr_uuid = gr.Text(value='', visible=False)
                gr_predict = gr.Label(label=predict_label)
                gr_explanation = gr.TextArea(label=explanation_label)
                gr_next = gr.Button(next_label)


        def _next_question(uuid_):
            if not uuid_:
                uuid_ = str(uuid.uuid4())
            global _QUESTION_IDS
            _qid = _QUESTION_IDS.get(uuid_, -1)
            _qid += 1
            _QUESTION_IDS[uuid_] = _qid

            if _qid >= len(_QUESTIONS):
                del _QUESTION_IDS[uuid_]
                return game_cleared_label, '', '', {}, '', \
                    gr.Button(submit_label, interactive=False), \
                    gr.Button(try_again_label, interactive=True), \
                    ''
            else:
                executor = QuestionExecutor(_QUESTIONS[_qid], _LANG)
                return executor.question_text, '', '', {}, '', \
                    gr.Button(submit_label, interactive=True), \
                    gr.Button(next_label, interactive=False), \
                    uuid_


        gr_next.click(
            fn=_next_question,
            inputs=[gr_uuid],
            outputs=[
                gr_requirement, gr_question, gr_answer,
                gr_predict, gr_explanation, gr_submit, gr_next, gr_uuid,
            ],
        )


        def _submit_answer(qs_text: str, api_key: str, uuid_: str):
            if _need_api_key() and not api_key:
                raise gr.Error(api_error_info)

            _qid = _QUESTION_IDS[uuid_]
            executor = QuestionExecutor(
                _QUESTIONS[_qid], _LANG,
                llm=_LLM, llm_cfgs=_get_api_key_cfgs(api_key) if _need_api_key() else {}
            )
            answer_text, correctness, explanation = executor.check(qs_text)
            labels = {correct_label: 1.0} if correctness else {wrong_label: 1.0}
            if correctness:
                return answer_text, labels, explanation, gr.Button(next_label, interactive=True), uuid_
            else:
                return answer_text, labels, explanation, gr.Button(next_label, interactive=False), uuid_


        gr_submit.click(
            _submit_answer,
            inputs=[gr_question, gr_api_key, gr_uuid],
            outputs=[gr_answer, gr_predict, gr_explanation, gr_next, gr_uuid],
        )

    demo.launch()
