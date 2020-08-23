import tweepy
import logging
from credentials import *

logging.basicConfig(format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Adjust the values below to tweak the bot to your liking

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Keyword(s) and/or hashtag(s) that you want to like / retweet
# Basic Formatting:
#   - Use %20OR%20 to separate keywords and hashtags
#       - i.e. dog%20OR%20cat
#   - Replace hashtag symbol # with %23 
#       - i.e. #twitter should be %23twitter
# More information about query formatting here: 
#   https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/basic-stream-parameters
search_keywords = "%22animal crossing%22celeste"

# Time to wait between processing a request in seconds 
# Information about TwitterAPI limits here: https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits
delay = 100

# Specify what type of search results you want to get
# 'recent', 'popular', or 'mixed'
result_type = 'mixed'

# Specify the number of tweets you want the bot to iterate through
number_of_tweets = 5
# OR change run_continuously to True if you want it to run continuously (or for deploying)
# if True, number_of_tweets will not be used
run_continuously = True

# Change booleans depending on if you want to only retweet, only like, or do both
retweet_tweets = True
like_tweets = True


def create_api():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_KEY_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error('Authentication Error', exc_info=True)
        raise e
    logger.info(f"Authentication OK. Connected to @{api.me().screen_name}")

    return api
