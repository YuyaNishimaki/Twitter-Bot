# Twitter-Bot
## 実行

```
$ python main.py
```

## デプロイ
pushした時に、自動でHerokuにデプロイされる。\
手動でデプロイする場合は
https://dashboard.heroku.com/apps/blooming-hollows-25761/deploy/github
からデプロイする。\
以下のようにしてCLIでデプロイすることもできる。

```
git add -A
git commit -m "commit message"
git push heroku master
```

## プログラム説明
- Procfile・requirements.txt・index.py・runtime.txt\
デプロイする時に追加で必要なファイル群。

- user_ids.txt\
QiitaのユーザID一覧。ユーザに変更があれば、適宜更新する。

- tweeted_learning_blog_urls.txt\
すでに投稿済の学びブログのURLリスト。

- execution_datetime.py\
前回スクリプトを実行した日時の記録や、読み込みを行う。
