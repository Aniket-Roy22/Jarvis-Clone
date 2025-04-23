import requests
import json
import os

def aiResponse(prompt: str) -> str:
    response = requests.post (
        url="https://openrouter.ai/api/v1/chat/completions",
        headers =
        {
            "Authorization": "Bearer " + os.getenv("deepseek-client-key"),
            "Content-Type": "application/json",
        },
        data=json.dumps(
        {
            "model": "deepseek/deepseek-r1-distill-llama-70b:free",
            "messages": [
            {
                "role": "user",
                "content": prompt,
            }],
        })
    )
    return response.json()["choices"][0]["message"]["content"]