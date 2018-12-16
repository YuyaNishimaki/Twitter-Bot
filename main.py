import config
from twitter import Twitter, OAuth
import http.client
import json


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
    # print(res.status, res.reason)
    data = response.read().decode("utf-8")
    jsonstr = json.loads(data)
    url = jsonstr[0]["url"]
    return url


def main():
    t = Twitter(
        auth=OAuth(
            config.TW_TOKEN,
            config.TW_TOKEN_SECRET,
            config.TW_CONSUMER_KEY,
            config.TW_CONSUMER_SECRET,
        )
    )

    USER_ID = "macky4"
    ITEM_NUM = 10
    PAGE = "1"
    PAR_PAGE = "10"

    response = connect_qiita(USER_ID, PAGE, PAR_PAGE)
    url = get_url(response)

    # msg = "テスト投稿ですm(_ _)m"
    # t.statuses.update(status=msg)


if __name__ == "__main__":
    main()
