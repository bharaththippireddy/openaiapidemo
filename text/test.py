import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Embedding.create(
  input="Learn Share and Grow",
  model="text-embedding-ada-002"
)

print(response)