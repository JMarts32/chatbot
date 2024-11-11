import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']=os.getenv('LANGCHAIN_TRACING_V2')
os.environ['LANGCHAIN_ENDPOINT']=os.getenv('LANGCHAIN_ENDPOINT')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')

'''
@Example of the prompt
'''
messages = [
    {"role": "system", "content": "Eres Juan"},
    {"role": "user", "content": "Hola Juan"},
    {"role": "system", "content": "Hola!"},
    {"role": "user", "content": "Como te llamas?"}
]

'''
How to sent it
'''
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)
print(response.choices[0].message.content)