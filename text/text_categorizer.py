import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=100,
    temperature=0.5,
    messages=[{'role':'user','content':
        'categorize the following companies.'
        'Microsoft Corporation, Roche Holding AG, Apple Inc, Amazon.com, Inc,Pfizer Inc, JPMorgan Chase & Co.,Johnson & Johnson, Bank of America Corporation, Industrial and Commercial Bank of China .'}]
)

print(response["choices"][0]["message"]["content"])