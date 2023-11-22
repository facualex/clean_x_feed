
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

# @desc: Get links for tweets, retweets, and comments
def get_tweets_links(user_name, data_path = f'{PROJECT_ROOT}/data/tweet-headers.js'):
    tweets = js_json_to_py_json(data_path = data_path)
    tweet_links = []

    for tweet in tweets:
        tweet_id = tweet['tweet']['tweet_id']

        tweet_links.append(f"https://twitter.com/{user_name}/status/{tweet_id}")

    return tweet_links