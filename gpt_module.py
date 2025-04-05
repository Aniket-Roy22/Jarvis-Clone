from g4f.client import Client

def aiResponse(prompt: str) -> str:
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        web_search=False
    )
    return response.choices[0].message.content

# def main():
#     prompt: str = input("Enter your query: ")
#     briefPromt: str = prompt + "\nplease respond very briefly."
    
#     global response
#     response = aiResponse(briefPromt)
    
# if __name__ == '__main__':
#     main()