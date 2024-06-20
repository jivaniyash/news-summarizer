import openai
import time

import os
from dotenv import load_dotenv
load_dotenv()
    
def generate_summary(news_article:str, character_limit: int, tone:str):
    '''Function to call APIs'''
        
    # my_api_key = os.getenv("OPENAI_API_KEY")
    client= openai.Client()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages= [
            {"role": "system", "content": "You are an assistant to help users to generate short summary of a news article based on requirements. You need to adjust tone of the output based on the users request. Character limit includes spaces, punctuations, words. Just provide the final output. Verify the summary is less than {character_limit} characters and make adjustments as needed. Don't output character count"},
            {"role": "user", "content": f"I want a summary from the given News Article for {tone} tone & LIMIT output to {character_limit} characters. Here is the News Article: \n {news_article}"}
        ]
    )
    
    try:
        summary = response.choices[0].message.content
        return summary
    except Exception as error:
        return f"There is error in generating summary - {error}"