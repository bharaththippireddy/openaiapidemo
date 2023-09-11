import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Image.create_edit(
    prompt="A big house with a tube in the swimming pool",
    image=open("housewithpool.png",mode="rb"),
    mask=open("masked.png",mode="rb"),
    n=1,
    size="1024x1024"
)
print(response)
