import os
import uuid

import gradio as gr

from llmriddles.questions import QuestionExecutor
from llmriddles.questions import list_ordered_questions

_QUESTION_IDS = {}
_QUESTIONS = list_ordered_questions()
_LANG = os.environ.get('QUESTION_LANG', 'cn')
_LLM = os.environ.get('QUESTION_LLM', 'chatgpt')


def _need_api_key():
    return _LLM == 'chatgpt'


def _get_api_key_cfgs(api_key):
    if _LLM == 'chatgpt':
        return {'api_key': api_key}
    else:
        return {}


if __name__ == '__main__':
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                gr_requirement = gr.TextArea(placeholder='Click \'Next\' to Start', label='Requirements')
                gr_question = gr.TextArea(placeholder='Your Question for LLM', label='Question')
                gr_answer = gr.TextArea(placeholder='Answer From LLM', label='Answer')
                gr_submit = gr.Button('Submit', interactive=False)

            with gr.Column():
                gr_api_key = gr.Text(placeholder='Your API Key', label='API Key', type='password',
                                     visible=_need_api_key())
                gr_uuid = gr.Text(value='', visible=False)
                gr_predict = gr.Label(label='Correctness')
                gr_explanation = gr.TextArea(label='Explanation')
                gr_next = gr.Button('Next')


        def _next_question(uuid_):
            if not uuid_:
                uuid_ = str(uuid.uuid4())
            global _QUESTION_IDS
            _qid = _QUESTION_IDS.get(uuid_, -1)
            _qid += 1
            _QUESTION_IDS[uuid_] = _qid
            print(_QUESTION_IDS)

            if _qid >= len(_QUESTIONS):
                del _QUESTION_IDS[uuid_]
                return 'Congratulations!', '', '', {}, '', \
                    gr.Button('Submit', interactive=False), \
                    gr.Button('Try Again', interactive=True), \
                    ''
            else:
                executor = QuestionExecutor(_QUESTIONS[_qid], _LANG)
                return executor.question_text, '', '', {}, '', \
                    gr.Button('Submit', interactive=True), \
                    gr.Button('Next', interactive=False), \
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
                return '---', {}, 'Please Enter API Key Before Submitting Question.', \
                    gr.Button('Next', interactive=False), uuid_

            print(_QUESTION_IDS)
            _qid = _QUESTION_IDS[uuid_]
            executor = QuestionExecutor(
                _QUESTIONS[_qid], _LANG,
                llm=_LLM, llm_cfgs=_get_api_key_cfgs(api_key) if _need_api_key() else {}
            )
            answer_text, correctness, explanation = executor.check(qs_text)
            labels = {'Correct': 1.0} if correctness else {'Wrong': 1.0}
            if correctness:
                return answer_text, labels, explanation, gr.Button('Next', interactive=True), uuid_
            else:
                return answer_text, labels, explanation, gr.Button('Next', interactive=False), uuid_


        gr_submit.click(
            _submit_answer,
            inputs=[gr_question, gr_api_key, gr_uuid],
            outputs=[gr_answer, gr_predict, gr_explanation, gr_next, gr_uuid],
        )

    demo.launch()
