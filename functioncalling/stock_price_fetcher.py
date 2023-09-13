import os
import openai
import json

openai.api_key = os.environ['OPENAI_API_KEY']

def get_stock_price(symbol):
    """Get the current stock price for given symbol"""
    stock_info = {
        "symbol": symbol,
        "price": "1000"
    }
    return json.dumps(stock_info)


functions = [
    {
        "name": "get_stock_price",
        "description": "Get the current stock price for the given symbol",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The symbol, e.g. AAPL",
                }
            },
            "required": ["symbol"],
        },
    }
]


messages = [{'role': 'user', 'content': 'Get stock symbol and price for Apple'}]

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=messages,
    functions=functions,
    function_call="auto"
)
response_message = response['choices'][0]['message']
if response_message.get('function_call'):
    function_args = json.loads(response_message['function_call']['arguments'])
    print(get_stock_price(function_args.get('symbol')))

#print(response['choices'][0]['message'])
#print(response['choices'][0]['message']['content'])

