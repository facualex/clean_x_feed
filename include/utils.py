def get_project_root_path():
    import os
    current_file_path = os.path.abspath(__file__)
    return os.path.dirname(os.path.dirname(current_file_path))

# TODO: Abstract further. Create function to transform js json to py json and
# this one should just use it to transform each json element of the array.
PROJECT_ROOT = get_project_root_path()
def js_json_to_py_json(data_path = f'{PROJECT_ROOT}/data/tweet-headers.js'):
    import json

    # Read the .js file
    with open(data_path, 'r') as file:
        # Extract the JavaScript variable assignment and remove the 'window.YTD.tweet_headers.part0 =' part
        js_data = file.read().split('=')[1]

        # Convert JavaScript-style single quotes to double quotes
        js_data = js_data.replace("'", '"')

        # Parse the JSON data
        data_list = json.loads(js_data)

    # Now 'data_list' contains a list of dictionaries, each representing a JSON object
    return data_list

# @desc: Get urls for tweets, retweets, and comments
# @return: string[] - list of urls 
def get_tweets_urls(data_path = f'{PROJECT_ROOT}/data/tweet-headers.js'):
    import os

    tweets = js_json_to_py_json(data_path = data_path)
    tweet_links = []

    for tweet in tweets:
        tweet_id = tweet['tweet']['tweet_id']

        tweet_links.append(f"https://twitter.com/{os.environ.get('X_USERNAME')}/status/{tweet_id}")

    return tweet_links

##################################
#### SELENIUM UTILITY FUNCTIONS ##
##################################

class ResourceNotFound(Exception):
    pass

def x_login():
    import time
    import os
    from selenium import webdriver
    from selenium.webdriver import ChromeOptions, Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.chrome.service import Service

    service = Service()
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options, service=service)
    url = "https://twitter.com/i/flow/login"
    driver.get(url)

    username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
    username.send_keys(os.environ.get('X_USERNAME'))
    username.send_keys(Keys.ENTER)

    password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
    password.send_keys(os.environ.get('X_PASSWORD'))
    password.send_keys(Keys.ENTER)

    time.sleep(10)

    return driver

# TODO: Check resource existence. Get URL and check if it's a valid resource.
def check_resource_existence(resource_url):
    try:
        a = 5

        # <a href="/search" role="link"> => if this element exists, then the resource was not found. 
        # This element is the "Search" blue button that shows in the screen when a post was not found.
        does_resource_exists = True

        if not does_resource_exists:
            raise ResourceNotFound(f"The following resource doesn't exist: {resource_url}")
        
        # The resource exists, but MIGHT NOT BE YOURS 
        return True
    except ResourceNotFound as resource_error:
        print(resource_error)
        return False

# @desc: Delete tweet (comment or post)
def delete_resource(tweet_url):
    does_resource_exists = check_resource_existence('http://twitter.com/mate_head/status/3')

    # Just try to delete the tweet, if the Delete button is found, then its a comment or post of yours.
    # If it's not found, then it's a retweet.
    return True

# @desc: Delete retweet
def delete_retweet(retweet_url):
    return True

# popup menu btn => <div aria-expanded="false" aria-haspopup="menu" aria-label="Más opciones" role="button" tabindex="0" data-testid="caret">