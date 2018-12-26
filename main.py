from qiita_blog import tweet_qiita_url
from learning_blog import tweet_learning_blog_url
from execution_datetime import write


def main():
    tweet_qiita_url()
    write()
    print("Qiita終了")
    tweet_learning_blog_url()
    print("学びブログ終了")


if __name__ == "__main__":
    main()
