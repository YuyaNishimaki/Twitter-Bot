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


def get_urls(response):
    print(response)
    data = response.read().decode("utf-8")
    jsonstrs = json.loads(data)
    past_time = load_execution_datetime()
    urls = [
        jsonstr["url"]
        for jsonstr in jsonstrs
        if datetime.datetime.strptime(
            jsonstr["created_at"], "%Y-%m-%dT%H:%M:%S+09:00"
        )  # noqa E501
        > past_time
    ]
    return urls


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
        datetime_dt = datetime.datetime.strptime(
            datetime_str, "%Y-%m-%d %H:%M:%S"
        )  # noqa #501
        return datetime_dt
    except FileNotFoundError:
        return datetime.datetime(2018, 12, 1, 0, 0, 0)


def tweet_qiita_url():
    PAGE = "1"
    PAR_PAGE = "10"
    for USER_ID in load_user_ids():
        response = connect_qiita(USER_ID, PAGE, PAR_PAGE)
        urls = get_urls(response)
        import ipdb

        ipdb.set_trace()
        print(urls)
        # for url in urls:
        #     tweet(url)


def main():
    write_execution_datetime()
    tweet_qiita_url()


if __name__ == "__main__":
    main()
