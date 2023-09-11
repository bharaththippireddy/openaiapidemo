import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    max_tokens=100,
    messages=[{'role':'user','content':'how to make a cake'}],
    n=3
)

for choice in response.choices:
    print(choice.message.content)