import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Moderation.create(
    model='text-moderation-latest',
    #input='My favorite movie is kill bill'
    input='I hate myself and want to harm myself'
)

print(response)
print(response["results"][0]["flagged"])
print(response["results"][0]["categories"])
print(response["results"][0]["category_scores"])
print(response["results"][0]["categories"]["self-harm"])
print(response["results"][0]["category_scores"]["self-harm"])