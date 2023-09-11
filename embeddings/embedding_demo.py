import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

response = openai.Embedding.create(
    input="learn share and grow",
    model="text-embedding-ada-002"
)

print(response)
print(response['data'][0]['embedding'])
