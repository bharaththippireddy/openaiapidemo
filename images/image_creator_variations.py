import os
import openai
from base64 import b64decode

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Image.create_variation(
    image=open("ferrari.png", mode="rb"),
    n=2,
    size="256x256",
)

print(response)