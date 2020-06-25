# bot.py
import tweepy
import logging
import json
import time
from config import create_api
from db import select_quote

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_mentions(api, since_id):
    """
    This function gets an api object and a twitter id and search for new mentions
    since that last (already replied) and so replies all
    """
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        if tweet.user.id != 1269312077174394882:
            new_since_id = max(tweet.id, new_since_id)
            logger.info(f"Answering to {tweet.user.name}")
            quote = select_quote()
            api.update_status(
                status=f"@{tweet.user.screen_name} {quote}", in_reply_to_status_id=tweet.id)
    return new_since_id


def main():
    with open('bot/data/last_since_id.json', 'r') as f:
        last_since_id = json.load(f)
    api = create_api()
    since_id = int(last_since_id['last_since_id'])
    while True:
        since_id = check_mentions(api, since_id)
        logger.info("Waiting...")
        with open('bot/data/last_since_id.json', 'w') as f:
            json.dump({'last_since_id': str(since_id)}, f)
        time.sleep(60)


if __name__ == "__main__":
    main()
