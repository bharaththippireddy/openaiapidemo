import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    max_tokens=100,
    messages=[{'role':'user','content':'What is OpenAI?'}],
    stream=True
)

print(type(response))
for each_chunk in response:
    chunk_message=each_chunk["choices"][0]["delta"]
    print(chunk_message.get('content',''))
