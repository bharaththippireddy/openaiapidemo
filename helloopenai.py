import os
import openai
import tiktoken

openai.api_key = os.environ['OPENAI_API_KEY']

tokenizer = tiktoken.get_encoding("cl100k_base")
print(tokenizer.encode("company"))

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    max_tokens=100,
    #stop = ["research","artificial"],
    #temperature = 1,
    top_p=0.9,
    presence_penalty=0.9,
    frequency_penalty=1,
    logit_bias={tokenizer.encode("company")[0]: -100},
    messages=[{'role':'user','content':'What is OpenAI?'}]
)
print(response)
print(type(response))
print(response['model'])
print(response['choices'][0]['message']['content'])