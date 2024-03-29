# DB関連
from sqlalchemy import Column
from sqlalchemy import Integer,BigInteger,String,DateTime,Time,Double,Boolean
from sqlalchemy import func
from sqlalchemy import or_,and_
from sqlalchemy import insert

from sqlalchemy.future import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

#日付関連
from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=9),"JST")

#定期実行関連
import schedule
import time

#その他
import sys
import requests

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
    connection = os.environ["Connection"]
    webhook_url = os.environ["webhook_url"]
except Exception as e:
    print(f"エラー：{e} (L34)")
#----
    
#DB接続
engine = create_engine(f"mysql+pymysql://{db_user}:{db_passwd}@{db_address}/{db_name}?charset=utf8")
Base = declarative_base()
#-----

#テーブル情報
class HttpLog(Base):
    __tablename__ = db_table
    id = Column("id", BigInteger, primary_key=True)
    date = Column("date",DateTime)
    time = Column("time",Time)
    response_code = Column("response_code",Integer)
    response_time = Column("response_time",Double)
    response_result = Column("response_result",Boolean)
#----

Session = sessionmaker(bind=engine)
session = Session()

print(f"{datetime.now(JST)} プログラムを開始しました")

def main():
    # 今の時間の日付
    today = datetime.now(JST)
    time = today.time()
    #----

    print(f"{today} リクエストを実行します")

    #HTTP通信を行う
    #チェック対象のWebサーバーに向けてGETリクエストを送信する
    #ResponseCodeと時間を取得する
    url = f"http://{connection}"
    header = {"User-Agent":"Python3-Requests/2.31.0"}
    try:
        response = requests.get(url,headers=header)
    except Exception as e:
        print(f"エラー：{e} (L79)")
        sys.exit(1)
    #----

    #DBに書き込む処理
    try:
        
        DBdata = HttpLog()
        DBdata.date = today
        DBdata.time = time
        DBdata.response_code = response.status_code
        DBdata.response_time = response.elapsed.total_seconds()

        if response.status_code == requests.codes.ok:
            DBdata.response_result = True
        else:
            DBdata.response_result = False
        
        session.add(DBdata)
        session.commit()
        
    except Exception as e:
        print(f"エラー：{e} (writeDB)")
    finally:
        session.close()
        print(f"{today} 処理が終了しました")
    #----
          
#2分毎に実行する
schedule.every(2).minutes.do(main)
while True:
    schedule.run_pending()
    time.sleep(1)
#----