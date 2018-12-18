import config
from twitter import Twitter, OAuth
import http.client
import json
import datetime
import pathlib


def connect_qiita(uid, page, ppage):
    conn = http.client.HTTPSConnection("qiita.com", 443)
    conn.request(
        "GET",
        "/api/v2/users/"
        + uid
        + "/items?page="
        + page
        + "&per_page="
        + ppage,  # noqa E501
    )
    res = conn.getresponse()
    return res


def get_url(response):
    # print(response.status, response.reason)
    data = response.read().decode("utf-8")
    jsonstr = json.loads(data)
    # print(json.dumps(jsonstr, indent=4))
    url = jsonstr[0]["url"]
    return url


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


def load_user_ids():
    path = pathlib.Path("user_ids.txt")
    user_ids = [user_id.strip() for user_id in path.read_text().split()]

    return user_ids


def write_execution_datetime():
    path = pathlib.Path("exexcution_datetime.txt")
    dt_now = datetime.datetime.now()
    path.write_text(dt_now.strftime("%Y-%m-%d %H:%M:%S"))


def load_execution_datetime():
    path = pathlib.Path("exexcution_datetime.txt")
    try:
        datetime_str = path.read_text()
        datetime_dt = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    except FileNotFoundError:
        pass


def main():
    user_ids = load_user_ids()
    load_execution_datetime()
    write_execution_datetime()
    USER_ID = "macky4"
    PAGE = "1"
    PAR_PAGE = "10"

    # response = connect_qiita(USER_ID, PAGE, PAR_PAGE)
    # url = get_url(response)
    # msg = url
    # tweet(msg)


if __name__ == "__main__":
    main()
