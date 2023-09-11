import openai, numpy as np
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

resp = openai.Embedding.create(
  input=["you are awesome", "you are good"],
  engine="text-similarity-davinci-001"
)

embedding_a = resp['data'][0]['embedding']
embedding_b = resp['data'][1]['embedding']
similarity_score = np.dot(embedding_a, embedding_b)

print(similarity_score*100,"%")