import zhipuai
from .base import register_llm


def ask_chatglm(message: str, api_key: str):
    zhipuai.api_key = api_key

    response = zhipuai.model_api.invoke(
        model="chatglm_turbo",
        prompt=[{
            "role": "user",
            "content": message
        }],
        top_p=0.7,
        temperature=0.9,
    )

    response_msg = response['data']['choices'][0]['content']
    # strip the front and end '"'
    if len(response_msg) >= 2:
        response_msg = response_msg[1:-1]

    return response_msg


register_llm('chatglm', ask_chatglm)
