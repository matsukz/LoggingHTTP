# DB関連
from sqlalchemy import Column
from sqlalchemy import Integer,BigInteger,String,DateTime
from sqlalchemy import func
from sqlalchemy import or_,and_

from sqlalchemy.future import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

#日付関連
from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=9),"JST")

#その他
import sys
import requests
import ping3

#環境変数関連
import os
from dotenv import load_dotenv
try:
    load_dotenv()
    db_address = os.environ["db_address"]
    db_name = os.environ["db_name"]
    db_table = os.environ["db_table"]
    db_user = os.environ["db_user"]
    db_passwd = os.environ["db_passwd"]
    webhook_url = os.environ["webhook_url"]
except Exception as e:
    print(f"エラー：{e}")
#----

# 今の時間の日付
today:datetime
time:datetime
today = datetime.now(JST)
time = today.time()
#print(time)
#----

#HTTP通信を行う
#チェック対象のWebサーバーに向けてGETリクエストを送信する
#ResponseCodeと時間を取得する
url = "http://100.96.0.1/check_warp"
header = {"User-Agent":"Python3-Requests/2.31.0"}
response = requests.get(url,headers=header)

#print(f"respcode={response.status_code}\nresptime={response.elapsed.total_seconds()}")