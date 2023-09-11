import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

audio_file = open("sample_french.mp3", "rb")

response = openai.Audio.translate(
    model="whisper-1",
    file=audio_file
)

print(response)

