# WARPに接続できるかチェックしてDBに保存するやーつ

* WARP-to-WARPを経由してHTTP接続できるかテストするやつです。
* PINGでも良かったのですが、L3以上でトラブることも多かったので

# 起動
* `git clone`します
* 以下の場所にディレクトリやファイルを作成します
* 不足した情報は自分で追記します
  * mysql/data
    * 中身なし
  * mysql/.env
    ```env
    MYSQL_DATABASE=HTTP_Log
    MYSQL_USER=
    MYSQL_PASSWORD=
    MYSQL_ROOT_PASSWORD=
    TZ=Asia/Tokyo
    ```
  * phpmyadmin/.env
    ```.env
    PMA_ARBITRARY=1
    PMA_HOST=mysql
    PMA_USER=
    PMA_PASSWORD=
    TZ=Asia/Tokyo
    ```
  * python3/.env
    ```.env
    db_name=HTTP_Log
    db_table=
    db_user=
    db_passwd=
    db_address=mysql
    webhook_url=http://
    ```
* 起動コマンドを実行します
    ```bash
    docker-compose up -d
    ```
    * `docker-compose.yml`があるディレクトリで実行します
    * WindowsでもLinuxでも共通です