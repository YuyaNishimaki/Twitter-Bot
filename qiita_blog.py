import http.client
import json
import datetime
import pathlib
from time import sleep
from tweet import tweet
from execution_datetime import load


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
    past_time = load()
    blog_data_list = [
        data
        for data in all_data
        if datetime.datetime.strptime(
            data["created_at"], "%Y-%m-%dT%H:%M:%S+09:00"
        )  # noqa E501
        > past_time
    ]
    return blog_data_list


def tweet_qiita_url():
    PAGE = "1"
    PAR_PAGE = "10"
    HASH_TAG = "\n#プログラミング "

    for USER_ID in load_user_ids():
        response = connect_qiita(USER_ID, PAGE, PAR_PAGE)
        blog_data_list = get_blog_data_list(response)

        post = 0
        for blog_data in blog_data_list:
            msg = blog_data["title"] + "\n\n"
            for tags in blog_data["tags"]:
                if len(msg + HASH_TAG + "#" + tags["name"] + " ") > 144:
                    break
                else:
                    HASH_TAG += "#" + tags["name"] + " "

            msg += HASH_TAG.strip(" ") + blog_data["url"]
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
