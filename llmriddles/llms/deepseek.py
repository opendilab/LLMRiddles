from openai import OpenAI
from .base import register_llm


def ask_deepseek(message: str, api_key: str) -> str:

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{
                "role": "user",
                "content": message
            }],
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "啊哦，请求出错啦，请重试一次。"


register_llm('deepseek', ask_deepseek)
