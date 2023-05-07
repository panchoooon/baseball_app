# baseball_app

1. サーバー起動
    1. Topのディレクトリである、baseball_appで以下コマンドを実行。  
    `python manage.py runserver`  
    すると、以下のようなエラーが出てくるので、エラーが出なくなるまで、該当ライブラリのインストール・runserverコマンド実行を繰り返す。
    > Cannot use XXXX because XXXX is not installed.

    2. アプリの移行を適用  
    上記で、エラーが出なくなると、サーバーが立ち上がるが、  
    以下のコマンドを、実行するように指示されるため、CTRL+Cで一度サーバーを停止し、指示通りに実行。  
    `python manage.py migrate`  
    アプリの移行が適用されるので、再度、以下コマンドを実行し、  
    `python manage.py runserver`  
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)へ移動し、Webアプリへの遷移を確認する。

2. sqliteの管理者ユーザー作成  
  ローカルDBのデータを見るための、管理者ユーザーを作成する。  
  Topのディレクトリである、baseball_appで以下コマンドを実行。  
  `python manage.py createsuperuser`  
  ユーザー名、メールアドレス（任意）、パスワード（英字＋数字）を入力し、アカウントを作成する。  
  サーバーを起動した状態で、  
  [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)へ移動し、作成した、ユーザー名・パスワードでログインが可能なことを確認する。
