import selenium
import os

from dotenv import load_dotenv
from include.utils import (get_tweets_urls,
                           delete_resource,
                           delete_retweet,
                           x_login)

def main_function():
    load_dotenv()

    tweet_links = get_tweets_urls(data_path='data/tweet-headers.js',)

    logged_in_instance = x_login()

    print(logged_in_instance.title)
    
    logged_in_instance.quit()

if __name__ == "__main__":
    main_function()

 