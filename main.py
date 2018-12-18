import config
from twitter import Twitter, OAuth
import http.client
import json
import datetime
import pathlib
from time import sleep


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
    assert res.status == 200, "Status Error"
    return res


def load_user_ids():
    path = pathlib.Path("user_ids.txt")
    user_ids = [user_id.strip() for user_id in path.read_text().split()]

    print(user_ids)
    return user_ids


def get_blog_data_list(response):
    all_data = json.loads(response.read().decode("utf-8"))
    past_time = load_execution_datetime()
    blog_data_list = [
        data
        for data in all_data
        if datetime.datetime.strptime(
            data["created_at"], "%Y-%m-%dT%H:%M:%S+09:00"
        )  # noqa E501
        > past_time
    ]
    return blog_data_list


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


def tweet_qiita_url():
    PAGE = "1"
    PAR_PAGE = "10"
    HASH_TAG = "\n#プログラミング "

    for USER_ID in load_user_ids():
        response = connect_qiita(USER_ID, PAGE, PAR_PAGE)
        blog_data_list = get_blog_data_list(response)

        post = 0
        for blog_data in blog_data_list:
            msg = blog_data["title"] + "\n" + blog_data["url"]
            for tags in blog_data["tags"]:
                if len(msg + HASH_TAG + "#" + tags["name"] + " ") > 144:
                    break
                else:
                    HASH_TAG += "#" + tags["name"] + " "

            msg += HASH_TAG.strip(" ")
            tweet(msg)
            post += 1
            print(
                USER_ID
                + ": "
                + blog_data["url"]
                + "("
                + str(post)
                + "/"
                + str(len(blog_data_list))
                + ")"
            )
            sleep(3600)


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
        return datetime.datetime(2018, 12, 10, 0, 0, 0)


def delete_execution_datetime():
    path = pathlib.Path("exexcution_datetime.txt")
    path.unlink()


def main():
    tweet_qiita_url()
    write_execution_datetime()


if __name__ == "__main__":
    main()
