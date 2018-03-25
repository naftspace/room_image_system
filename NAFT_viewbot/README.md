## 概要
このディレクトリには部室の写真をNAFT_viewというLINE botから確認するためのLINE botのプログラムが置いてあります．

NAFT_viewにテキスト，画像，スタンプのいずれかを送信すると，返信として，部室の画像を送るようにしてあります．

## 詳細
LINE messaging apiのドキュメントによると，画像を返信するには，画像URLを情報に加えて，返信すればよいです．

Google Driveにアップロードされた写真のURLは更新されても変わらないので，常に同じURLを返信するという単純なプログラムで目的は達成されることがわかります．

## このプログラムを動かすには
以下のファイルを下記通りに変更してください

<dl>
  <dt>line_api/line_api/settings.py</dt>
  <dd>SERVER_URL 変数の中に，使用するSERVERのURLを入れてください  
  Herokuを使用する場合は "(HEROKU ID).herokuapp.com"となります．  </dd>
  <dt>line_api/linebot/views.py</dt>
  <dd>ACCESS_TOKEN 変数の中に，LINE BOTのACCESS TOKENを入れ，  
  FILE_ID 変数の中にLINE BOTで返信したい写真のGoogle Drive FILE IDを入れてください．  
  参考：http://stshisho.blogspot.jp/2015/06/googlegoogle.html  </dd>
</dl>


# Heroku Django Starter Template

An utterly fantastic project starter template for Django 1.10.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment.

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Using Python 2.7?

Just update `runtime.txt` to `python-2.7.13` (no trailing spaces or newlines!).


## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
