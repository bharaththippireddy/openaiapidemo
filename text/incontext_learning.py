import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    #max_tokens=100,
    temperature=0.5,
    messages=[{'role':'system','content':'You are a python programming tutor'},
                {'role':'user','content':'Explain what the sum() function does'},
                {'role':'assistant','content':'The sum() function returns the '
                                              'sum of numbers in the list'},
                {'role':'user','content':'Explain what the len() function does'}]
)

print(response["choices"][0]["message"]["content"])