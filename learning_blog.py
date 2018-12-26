from urllib import request
from bs4 import BeautifulSoup
from tweet import tweet
from time import sleep
import pathlib


def get_learning_blog_urls():
    url = "https://www.miraidenshi-tech.jp/category/intern-program/"
    soup = BeautifulSoup(request.urlopen(url).read(), "html.parser")
    urls = [
        soup.select_one(
            "#Page-content > ul > li:nth-of-type(" + str(i) + ")"
        ).a.get(  # noqa E501
            "href"
        )
        for i in range(1, 4)
    ]
    print(urls)
    return urls


def write_tweeted_url(url):
    path = "tweeted_learning_blog_urls.txt"
    with open(path, mode="a") as f:
        f.write(url + "\n")


def load_tweeted_url():
    path = pathlib.Path("tweeted_learning_blog_urls.txt")
    tweeted_urls = [url for url in path.read_text().split()]
    return tweeted_urls


def tweet_learning_blog_url():
    HASH_TAG = "\n#プログラミング #インターン\n"
    urls = get_learning_blog_urls()

    for i, url in enumerate(urls):
        if url not in load_tweeted_url():
            soup = BeautifulSoup(request.urlopen(url).read(), "html.parser")
            title = soup.select_one(
                "#Single-content > div > div.single-title > h2"
            )  # noqa #501
            tweet(title.text + "\n\n" + HASH_TAG + url)
            write_tweeted_url(url)

            print(url + "(" + str(i + 1) + "/" + str(len(urls)) + ")")
            if (i + 1) == len(url):
                break
            else:
                sleep(7200)
        else:
            continue
