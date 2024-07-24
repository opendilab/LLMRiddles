
from openai import OpenAI
from .base import register_llm



def ask_deepseek(message: str, api_key: str):
    client = OpenAI(
                api_key=api_key,
                base_url="https://api.deepseek.com"
            )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": message}
        ],
    )
    return response.choices[0].message.content.strip()



register_llm('deepseek', ask_deepseek)



