import os
import openai
from pydub import AudioSegment

openai.api_key = os.environ["OPENAI_API_KEY"]

audio_file = AudioSegment.from_file("sample_french.mp3")
audio_chunks = audio_file[::2000]

transcribed_text = ''

for i,chunk in enumerate(audio_chunks):
    with open(f"chunk_{i}.mp3","wb") as chunk_file:
        chunk.export(chunk_file,format="mp3")
    with open(f"chunk_{i}.mp3","rb") as chunk_file:
        transcript = openai.Audio.transcribe("whisper-1",chunk_file)
        transcribed_text=transcribed_text+transcript["text"]

print(transcribed_text)

