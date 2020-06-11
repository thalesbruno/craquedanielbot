# A simple twitter bot
This is a quite simple twitter bot that check for mentions every 60s 
and reply it with a phrase randomly picked up from a database of quotes.

We're using [Tweepy](https://www.tweepy.org/) library for accessing the Twitter API. 

Here is an article from Real Python website [How to Make a Twitter Bot in Python With Tweepy
](https://realpython.com/twitter-bot-python-tweepy/) we used as reference. You will learn how to generate the credentials needed to manipulate your bot and another stuffs. Please check it out.


### Installation and usage

Install the virtual environment   
`python -m venv venv`

Activate the virtual environment   
`. venv/bin/activate`

Install the requirements   
`pip install -r requirements`

Instatiate a database (we're using sqlite3)   
`python bot/db_instatiate.py`

At this point we will have a quotes.db file created. So:

Populate the database from a txt file with a quote per line   
`python bot/db_populate.py`

### Twitter credentials
We put the credentials received from Twitter in a json file called credentials.json. The file content looks like you see below:

```
{
    "consumer_key": "xpto_consumer_key",
    "consumer_secret": "xpto_consumer_secret",
    "access_token": "xpto_access_token",
    "access_token_secret": "xpto_access_token_secret"
}
```

With both essential files created, the database and the credentials file, we can finally run our application:   
`python bot/bot.py`