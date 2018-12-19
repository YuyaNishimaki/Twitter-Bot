import config
from twitter import Twitter, OAuth


def connect_twitter():
    t = Twitter(
        auth=OAuth(
            config.TW_TOKEN,
            config.TW_TOKEN_SECRET,
            config.TW_CONSUMER_KEY,
            config.TW_CONSUMER_SECRET,
        )
    )
    return t


def tweet(message):
    t = connect_twitter()
    t.statuses.update(status=message)
