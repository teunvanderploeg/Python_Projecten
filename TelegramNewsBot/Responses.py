import requests
import Constants as keys
from datetime import datetime


def get_news_responses(input_text):
    user_massage = str(input_text).lower()
    today = datetime.today()
    date = today.strftime("%Y-%m-%d")

    if user_massage == '/news':
        response = requests.get(
            "https://newsapi.org/v2/everything?q=Tech&from=" + date + "&pageSize=1&apiKey=" + keys.NEWS_API_KEY)
        if response.status_code != 200:
            return 'Error with news server'

        content = response.json()
        return content['articles'][0]['title'] + '\n' + '<a href="' + content['articles'][0][
            'url'] + '">Link to Article</a> '
