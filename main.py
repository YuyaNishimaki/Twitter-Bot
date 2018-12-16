import config
from twitter import Twitter, OAuth


def main():
    t = Twitter(
        auth=OAuth(
            config.TW_TOKEN,
            config.TW_TOKEN_SECRET,
            config.TW_CONSUMER_KEY,
            config.TW_CONSUMER_SECRET,
        )
    )

    msg = "テスト投稿ですm(_ _)m"  # Post a message
    t.statuses.update(status=msg)


if __name__ == "__main__":
    main()
