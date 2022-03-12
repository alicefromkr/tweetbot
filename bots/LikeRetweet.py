import tweepy
import logging
from config import create_api
from threading import Timer


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# API 생성 
api = create_api()

def add_member(user):
    # the ID of the list
    list_id = 1479090571625250821
    
    # fetch the screen name
    screen_name = [user.screen_name]
    
    # add user to the list
    # 중복 유저 알아서 처리 하길래 예외처리 추가 안함
    api.add_list_members(list_id = list_id, screen_name = screen_name)
    logger.info(f"{screen_name} added to list")

        
def search_tweets():
    for tweet in api.search(q="#개발자_트친소", lang="ko", result_type="recent", count=100):
        
        # Check if it's not a retweeted tweet 
        if 'RT @' not in tweet.text:
            # Check it's not favorited
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    logger.info("Tweet has been favorited")
                except Exception as e:
                    logger.error("Error on fav", exc_info=False)
                    continue
            # Check if it's not retweeted
            if not tweet.retweeted:
                try:
                    tweet.retweet()
                    logger.info("Tweet has been retweeted")
                except Exception as e:
                    logger.error("Error on retweet", exc_info=False)
                    continue
            # If it includes "여성", then add user to the list
            if "여성" in tweet.text:
                add_member(tweet.user)


def run():
    timer = Timer(1800, run)
    search_tweets()
    timer.start()
if __name__ == "__main__":
    run()