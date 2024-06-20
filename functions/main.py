from functions.news_article_retreiver import get_news_article
from functions.openai_functions import generate_summary

def summarizer(category: str, date:str, character_limit: int, tone:str):
    '''Function to call APIs'''
    
    news_article = get_news_article(category, date)
    
    news_summary = generate_summary(news_article, character_limit, tone)

    return news_article, news_summary

