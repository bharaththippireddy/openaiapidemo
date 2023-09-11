import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=100,
    temperature=0.5,
    messages=[{'role':'user','content':
        'Classify the sentiment in the two statements.'
        'Good, i like the way the course designed. It is a quick recap of all the java concepts.thanks'
        'The quizzes can be better'}]
)

print(response["choices"][0]["message"]["content"])