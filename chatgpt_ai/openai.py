from dotenv import load_dotenv
import openai
import os

load_dotenv('.env.local')

openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):
    print('[QUESTION]:', prompt)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=500, 
    )

    response_dict = response.get("choices")
    print('[ANSWER]:', response_dict)
    if response_dict and len(response_dict)>0:
        prompt_response = response_dict[0]["text"]
    return prompt_response