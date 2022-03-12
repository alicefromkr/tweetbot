import tweepy
import logging


logger = logging.getLogger()

def create_api():
    # Input API Key
    consumer_key = ""
    # Input API Key Secret
    consumer_secret = ""

    # Input Access Token
    access_token = ""
    # Input Access Token Secret
    access_token_secret = ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api