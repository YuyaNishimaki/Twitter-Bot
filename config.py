import os
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())
TW_CONSUMER_KEY = os.environ.get(
    "CONSUMER_KEY", os.environ.get("TW_CONSUMER_KEY")
)  # noqa E501
TW_CONSUMER_SECRET = os.environ.get(
    "CONSUMER_SECRET", os.environ.get("TW_CONSUMER_SECRET")
)
TW_TOKEN = os.environ.get("ACCESS_TOKEN_KEY", os.environ.get("TW_TOKEN"))
TW_TOKEN_SECRET = os.environ.get(
    "ACCESS_TOKEN_SECRET", os.environ.get("TW_TOKEN_SECRET")
)
