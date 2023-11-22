import requests
import selenium
import os

from dotenv import load_dotenv
from include.utils import get_tweets_links

def main_function():
    load_dotenv()

    X_USERNAME = os.environ.get("X_USERNAME")

    tweet_links = get_tweets_links(user_name=X_USERNAME,
                                   data_path='data/tweet-headers.js',)
    
    print(tweet_links)

if __name__ == "__main__":
    main_function()