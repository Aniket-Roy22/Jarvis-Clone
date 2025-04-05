from g4f.client import Client

def aiResponse(prompt: str) -> str:
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        web_search=False
    )
    return response.choices[0].message.content