def get_news_article(category, date) -> str:
    # edit code to call apis for News Article Source
    # for demo purpose, I have created text files for each article in news directory.
    
    file_name = f'news/{category}/{date}.txt'
    with open(file_name, 'r') as f:
        news = f.readlines()
        formatted_news = ''
        for line in news:
            formatted_news += line.strip()
        return formatted_news