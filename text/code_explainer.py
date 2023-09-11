import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

instruction = """Explain what this Python code does in one sentence:
number = int(input("Enter a number:"))
primeFlag = True
for i in range(2, number):
    if number % i == 0:
        primeFlag = False
        break
if primeFlag == True:
    print(number, " is prime.")
else:
    print(number, " is not prime.")
"""
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=100,
    temperature=0.5,
    messages=[{'role':'system','content':'You are a python developer'},
              {'role':'user','content':instruction}]
)

print(response["choices"][0]["message"]["content"])