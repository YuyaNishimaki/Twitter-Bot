from qiita_blog import tweet_qiita_url
from learning_blog import tweet_learning_blog_url
from execution_datetime import write


def main():
    tweet_qiita_url()
    tweet_learning_blog_url()
    write()


if __name__ == "__main__":
    main()
