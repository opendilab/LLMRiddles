import os

import gradio as gr

from llmriddles.questions import QuestionExecutor
from llmriddles.questions import list_ordered_questions

_QUESTION_ID = -1
_QUESTIONS = list_ordered_questions()
_LANG = os.environ.get('QUESTION_LANG', 'cn')
_LLM = os.environ.get('QUESTION_LLM', 'chatgpt')

if __name__ == '__main__':
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                gr_requirement = gr.TextArea(placeholder='Click \'Next\' to Start', label='Requirements')
                gr_question = gr.TextArea(placeholder='Your Question for LLM', label='Question')
                gr_answer = gr.TextArea(placeholder='Answer From LLM', label='Answer')
                gr_submit = gr.Button('Submit', interactive=False)

            with gr.Column():
                gr_predict = gr.Label(label='Correctness')
                gr_explanation = gr.TextArea(label='Explanation')
                gr_next = gr.Button('Next')


        def _next_question():
            global _QUESTION_ID
            _QUESTION_ID += 1

            if _QUESTION_ID >= len(_QUESTIONS):
                return 'Congratulations!', '', '', {}, '', \
                    gr.Button('Submit', interactive=False), \
                    gr.Button('Next', interactive=False)
            else:
                executor = QuestionExecutor(_QUESTIONS[_QUESTION_ID], _LANG)
                return executor.question_text, '', '', {}, '', \
                    gr.Button('Submit', interactive=True), \
                    gr.Button('Next', interactive=False)


        gr_next.click(
            fn=_next_question,
            inputs=[],
            outputs=[gr_requirement, gr_question, gr_answer, gr_predict, gr_explanation, gr_submit, gr_next],
        )


        def _submit_answer(qs_text: str):
            executor = QuestionExecutor(_QUESTIONS[_QUESTION_ID], _LANG)
            answer_text, correctness, explanation = executor.check(qs_text)
            labels = {'Correct': 1.0} if correctness else {'Wrong': 1.0}
            if correctness:
                return answer_text, labels, explanation, gr.Button('Next', interactive=True)
            else:
                return answer_text, labels, explanation, gr.Button('Next', interactive=False)


        gr_submit.click(
            _submit_answer,
            inputs=[gr_question],
            outputs=[gr_answer, gr_predict, gr_explanation, gr_next],
        )

    demo.launch()
