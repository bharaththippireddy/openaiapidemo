import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

messages = [{'role': 'system', 'content': 'You are a math tutor'}]
user_msgs = ['Explain what pi is','Summarize this in two bullet points']

for each_msg in user_msgs:
    user_dict = {'role':'user','content':each_msg}
    messages.append(user_dict)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.5,
        messages=messages)
    assistant_dict = dict(response["choices"][0]["message"])
    messages.append(assistant_dict)

print(response)