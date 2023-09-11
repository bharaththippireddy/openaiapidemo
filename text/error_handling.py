import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

try:
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        max_tokens=100,
        messages=[{'role':'user','content':'What is OpenAI?'}]
    )
except openai.error.AuthenticationError as e:
    print(f"Authentication Error: {e}")
except openai.error.InvalidRequestError as e:
    print(f"Invalid Request Error: {e}")
except openai.error.APIError as e:
    print(f"API Error: {e}")
except openai.error.APIConnectionError as e:
    print(f"API Connection Error: {e}")
except openai.error.Timeout as e:
    print(f"Timeout Error: {e}")
except openai.error.ServiceUnavailableError as e:
    print(f"Service Unavailable Error: {e}")
except openai.error.RateLimitError as e:
    print(f"Rate Limit Error: {e}")

