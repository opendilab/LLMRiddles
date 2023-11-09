import logging
import os
import uuid

import gradio as gr

from llmriddles.questions import QuestionExecutor
from llmriddles.questions import list_ordered_questions

_QUESTION_SESSIONS = {}
count = 0
_QUESTIONS = list_ordered_questions()
_LANG = os.environ.get('QUESTION_LANG', 'cn')
assert _LANG in ['cn', 'en'], _LANG
_LLM = os.environ.get('QUESTION_LLM', 'chatgpt')
assert _LLM in ['chatgpt', 'chatglm', 'mistral-7b'], _LLM
_LLM_KEY = os.environ.get('QUESTION_LLM_KEY', None)
_DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'

if _DEBUG:
    logging.getLogger().setLevel(logging.INFO)
else:
    logging.getLogger().setLevel(logging.WARNING)
if _LANG == "cn":
    title = "完蛋！我被 LLM 拿捏了"
    requirement_ph = """
    <h2 style="color: #6d28d9;"> 欢迎来到 LLM Riddles! </h2>
    <h4> 你将通过本游戏对大语言模型产生更深刻的理解。在本游戏中，你需要构造一个提给语言大模型的问题，使得它回复的答案符合题目要求。点击<i>\"下一题\"</i> 即可开始游戏。</h4>
    """
    requirement_label = "游戏须知/说明"
    question_ph = "你对大语言模型的提问（例如：请你输出1+1=3）"
    question_label = "玩家提问栏"
    answer_ph = "大语言模型的回答"
    answer_label = "大语言模型回答栏"
    submit_label = "提交"
    next_label = "下一题"
    api_ph = "你个人的大语言模型 API Key (例如：ChatGPT)"
    api_label = "API key"
    predict_label = "结果正确性"
    explanation_label = "结果详细解释"
    game_cleared_label = "<h2 style='color: #6d28d9;'>祝贺！你已成功通关！</h2>"
    correct_label = "正确"
    wrong_label = "错误"
    api_error_info = "请在提交问题之前先输入你的 API Key"
    try_again_label = "再玩一次"
    select_label = "选择关卡（投机取巧需谨慎）"
    title_markdown = """
    <div align="center">
        <img src="https://raw.githubusercontent.com/opendilab/LLMRiddles/main/llmriddles/assets/banner.svg" width="80%" height="20%" alt="Banner Image">
    </div>
    <h2 style="text-align: center; color: black;"><a href="https://github.com/OpenDILab/LLMRiddles"> 🎭LLM Riddles：完蛋！我被 LLM 拿捏了</a></h2>
    <strong><h5 align="center"> 其他在线示例：中文在线试玩版本<a href="https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGLMCN">（OpenXLab）</a> | 中文在线试玩版本<a href="https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGLMCN">（Hugging Face）</a> <h5></strong>
    <strong><h5 align="center"> 更多不同语言模型的在线试玩 demo 可以访问 GitHub<a href="https://github.com/OpenDILab/LLMRiddles">源代码仓库</a>获取<h5></strong>
    <h5 align="center"> 如果你喜欢这个项目，请给我们在 GitHub 点个 star ✨ <a href="https://github.com/OpenDILab/LLMRiddles"> 代码仓库传送门 </a> 。我们将会持续保持更新。再次感谢游戏<a href="https://www.zhihu.com/people/haoqiang-fan"> 原作者 </a>的奇思妙想！  </h5>
    <strong><h5 align="center">注意：算法模型的输出可能包含一定的随机性。相关结果不代表任何开发者和相关 AI 服务的态度和意见。本项目开发者不对生成结果作任何保证，仅供娱乐。<h5></strong>
    """
    tos_markdown = """
    ### 使用条款
    玩家使用本服务须同意以下条款：
    该服务是一项探索性研究预览版，仅供非商业用途。它仅提供有限的安全措施，并可能生成令人反感的内容。不得将其用于任何非法、有害、暴力、种族主义等目的。该服务可能会收集玩家对话数据以供未来研究之用。
    如果您的游玩体验有不佳之处，请发送邮件至 opendilab@pjlab.org.cn ！ 我们将删除相关信息，并不断改进这个项目。
    为了获得最佳体验，请使用台式电脑进行此预览版游戏，因为移动设备可能会影响可视化效果。
    **版权所有 2023 OpenDILab。**
    """
elif _LANG == "en":
    title = "LLM Riddles: Oops! Rolling in LLM."
    requirement_ph = """
    <h2 style="color: #6d28d9;">Welcome to LLM Riddles! </h2>
    <h4> In this game, you'll gain a deeper understanding of language models. Your challenge is to create a question to ask a language model in a way that the answer it provides meets specific criteria. Click <i>\'Next\'</i> to Start</h4>
    """
    requirement_label = "Game Requirements"
    question_ph = "Your Question for LLM (e.g. Please print 1+1=3)"
    question_label = "Question"
    answer_ph = "Answer From LLM"
    answer_label = "Answer"
    submit_label = "Submit"
    next_label = "Next"
    api_ph = "Your API Key (e.g. ChatGPT)"
    api_label = "API key"
    predict_label = "Correctness"
    explanation_label = "Explanation"
    game_cleared_label = "<h2 style='color: #6d28d9;'>Congratulations!</h2>"
    correct_label = "Correct"
    wrong_label = "Wrong"
    api_error_info = "Please Enter API Key Before Submitting Question."
    try_again_label = "Try Again"
    select_label = "Select level"
    title_markdown = """
    <div align="center">
        <img src="https://raw.githubusercontent.com/opendilab/LLMRiddles/main/llmriddles/assets/banner.svg" width="80%" height="20%" alt="Banner Image">
    </div>
    <h2 style="text-align: center; color: black;"><a href="https://github.com/OpenDILab/LLMRiddles"> 🎭LLM Riddles: Oops! Rolling in LLM.</a></h2>
    <h5 align="center"> If you like our project, please give us a star ✨ on GitHub for latest update <a href="https://github.com/OpenDILab/LLMRiddles"> (Code Link) </a>. Thanks for the interesting idea of the original game <a href="https://www.zhihu.com/people/haoqiang-fan"> author </a>.  </h5>
    <strong><h5 align="center">Notice: The output is generated by algorithm scheme and may involve some randomness. It does not represent the attitudes and opinions of any developers and AI services in this project. We do not make any guarantees about the generated content.<h5></strong>
    """
    tos_markdown = """
    ### Terms of use
    By using this service, players are required to agree to the following terms:
    The service is a research preview intended for non-commercial use only. It only provides limited safety measures and may generate offensive content. It must not be used for any illegal, harmful, violent, racist, or sexual purposes. The service may collect user dialogue data for future research.
    Please send email to opendilab@pjlab.org.cn if you get any inappropriate answer! We will delete those and keep improving our moderator.
    For an optimal experience, please use desktop computers for this demo, as mobile devices may compromise its quality.
    **Copyright 2023 OpenDILab.**
    """
else:
    raise KeyError("invalid _LANG: {}".format(_LANG))


def _need_api_key():
    return (_LLM == 'chatgpt' or _LLM == 'chatglm') and _LLM_KEY is None


def _get_api_key_cfgs(api_key):
    if _LLM == 'chatgpt':
        return {'api_key': api_key}
    elif _LLM == 'chatglm':
        return {'api_key': api_key}
    else:
        return {}


if __name__ == '__main__':
    with gr.Blocks(title=title, theme='ParityError/Interstellar') as demo:
        gr.Markdown(title_markdown)

        with gr.Row():
            gr_requirement = gr.HTML(value=requirement_ph, label=requirement_label)
        with gr.Row():
            with gr.Column():
                gr_question = gr.TextArea(placeholder=question_ph, label=question_label)
                gr_api_key = gr.Text(placeholder=api_ph, label=api_label, type='password', visible=_need_api_key())
                with gr.Row():
                    gr_submit = gr.Button(submit_label, interactive=False)
                    gr_next = gr.Button(next_label)
                with gr.Row():
                    gr_select = gr.Radio(
                        choices=[(QuestionExecutor(q, _LANG).question_name, i) for i, q in enumerate(_QUESTIONS)],
                        label=select_label
                    )

            with gr.Column():
                gr_uuid = gr.Text(value='', visible=False)
                gr_predict = gr.Label(label=predict_label)
                gr_answer = gr.TextArea(label=answer_label, lines=3)
                gr_explanation = gr.TextArea(label=explanation_label, lines=1)
        gr.Markdown(tos_markdown)

        def _postprocess_question_text(question_text):
            if _LANG == 'cn':
                idx = question_text.find('，')
                question_title = question_text[:idx]
                former, latter = question_title.split('（')
                question_title = former + '：' + latter[:-1]
                question_text = f"<h2 style='color: #6d28d9;'>{question_title}</h2><h4>{question_text[idx+1:]}</h4>"
            elif _LANG == 'en':
                idx = question_text.find(',')
                question_text = f"<h2 style='color: #6d28d9;'>{question_text[:idx]}</h2><h4>{question_text[idx+1:]}</h4>"
            return question_text


        def _radio_select(uuid_, select_qid):
            global count
            if not uuid_:
                uuid_ = str(uuid.uuid4())
                count += 1
                logging.info(f'Player {count} starts the game now')
            global _QUESTION_SESSIONS
            if uuid_ not in _QUESTION_SESSIONS:
                _QUESTION_SESSIONS[uuid_] = set(), select_qid
            else:
                _exists, _ = _QUESTION_SESSIONS[uuid_]
                _QUESTION_SESSIONS[uuid_] = _exists, select_qid

            executor = QuestionExecutor(_QUESTIONS[select_qid], _LANG)
            question_text = _postprocess_question_text(executor.question_text)
            return question_text, '', '', {}, '', \
                gr.Button(submit_label, interactive=True), \
                gr.Button(next_label, interactive=False), \
                uuid_

        gr_select.select(
            _radio_select,
            inputs=[gr_uuid, gr_select],
            outputs=[
                gr_requirement, gr_question, gr_answer,
                gr_predict, gr_explanation, gr_submit, gr_next, gr_uuid,
            ],
        )


        def _next_question(uuid_):
            global count
            if not uuid_:
                uuid_ = str(uuid.uuid4())
                count += 1
                logging.info(f'Player {count} starts the game now')
            global _QUESTION_SESSIONS
            if uuid_ in _QUESTION_SESSIONS:
                _exists, _qid = _QUESTION_SESSIONS[uuid_]
            else:
                _exists, _qid = set(), -1
            _qid += 1
            _QUESTION_SESSIONS[uuid_] = _exists, _qid

            if _qid >= len(_QUESTIONS):
                del _QUESTION_SESSIONS[uuid_]
                logging.info(f'Player {count} has passed the game now')
                return game_cleared_label, '', '', {}, '', \
                    gr.Button(submit_label, interactive=False), \
                    gr.Button(try_again_label, interactive=True), \
                    '', \
                    gr.Radio(
                        choices=[(QuestionExecutor(q, _LANG).question_name, i) for i, q in enumerate(_QUESTIONS)],
                        label=select_label
                    )
            else:
                executor = QuestionExecutor(_QUESTIONS[_qid], _LANG)
                question_text = _postprocess_question_text(executor.question_text)
                return question_text, '', '', {}, '', \
                    gr.Button(submit_label, interactive=True), \
                    gr.Button(next_label, interactive=False), \
                    uuid_, \
                    gr.Radio(
                        choices=[(QuestionExecutor(q, _LANG).question_name, i) for i, q in enumerate(_QUESTIONS)],
                        value=_qid,
                        label=select_label,
                    )


        gr_next.click(
            fn=_next_question,
            inputs=[gr_uuid],
            outputs=[
                gr_requirement, gr_question, gr_answer,
                gr_predict, gr_explanation, gr_submit, gr_next,
                gr_uuid, gr_select,
            ],
        )


        def _submit_answer(qs_text: str, api_key: str, uuid_: str):
            global _QUESTION_SESSIONS
            if _need_api_key() and not api_key:
                raise gr.Error(api_error_info)

            _exists, _qid = _QUESTION_SESSIONS[uuid_]
            executor = QuestionExecutor(
                _QUESTIONS[_qid], _LANG,
                llm=_LLM, llm_cfgs=_get_api_key_cfgs(api_key) if _need_api_key() else {'api_key': _LLM_KEY}
            )
            answer_text, correctness, explanation = executor.check(qs_text)
            labels = {correct_label: 1.0} if correctness else {wrong_label: 1.0}
            if correctness:
                _QUESTION_SESSIONS[uuid_] = (_exists | {_qid}), _qid
                return answer_text, labels, explanation, gr.Button(next_label, interactive=True), uuid_
            else:
                return answer_text, labels, explanation, gr.Button(next_label, interactive=False), uuid_


        gr_submit.click(
            _submit_answer,
            inputs=[gr_question, gr_api_key, gr_uuid],
            outputs=[gr_answer, gr_predict, gr_explanation, gr_next, gr_uuid],
        )

    concurrency = int(os.environ.get('CONCURRENCY', os.cpu_count()))
    favicon_path = os.path.join(os.path.dirname(__file__), 'llmriddles', 'assets', 'avatar.png')
    demo.queue().launch(max_threads=concurrency, favicon_path=favicon_path, share=True)
