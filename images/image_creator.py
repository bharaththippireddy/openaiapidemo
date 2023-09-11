import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Image.create(
    prompt="Programmer on the moon",
    n=3,
    size="1024x1024",
)

print(response)