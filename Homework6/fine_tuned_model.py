import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

# for homework 6, please change this to your own model
model_name = 'ft:gpt-3.5-turbo-1106:personal::99LPYTTC'

template = '''You are a Q&A bot. You provide short answers to questions.
For example:
Question: What does ASL stand for? American Sign Language.
Provide the answer to the following question:
Question: '''

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    message = [{'role': 'user', 'content': template + prompt}]

    response = openai.chat.completions.create(
        model = model_name,
        temperature = 0,
        stop = ['\n'],
        messages = message)

    print("assistant: " + response.choices[0].message.content)