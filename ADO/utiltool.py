import datetime
import os
import pickle
from DB import DB
import datetime
import pandas as pd

import requests
from qiyechatutil import Weichat


def getDatenow(days_delta=None):
    ''' 获取现在的时间'''
    t = datetime.datetime.now().strftime("%Y%m%d") if None == days_delta else (datetime.datetime.now()+datetime.timedelta(days=days_delta)).strftime("%Y%m%d")
    return t


def loadpickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def savePickle(path, name, dates):
    with open(os.path.join(path, name), 'wb') as f:
        pickle.dump(dates, f)

def sendGroupNews(dt):
    uri = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=98253339-56d9-422a-bdff-8596abf7f8e1'
    dates = {
        "msgtype": "text",
        "text": {
            "content": "{0}".format(dt)
        }
    }
    resp = requests.post(uri, headers={'Content-Type': 'application/json'}, json=dates)


def save2db(sql, table=None):
    tb = 'testdb' if None == table else table
    testdb = DB(tb)
    testdb.connDb()

    print(sql)
    result = testdb.update(sql)
    # print(result[0][0])
    testdb.closeDb()

if __name__ == '__main__':
    # sendGroupNews('nes<br />&\ngt;sakdjh')

    from config import config
    res_path = config().res_path
    listfile = os.listdir(res_path)
    pickles = []
    for _ in listfile:
        print(_)
        if _.endswith('.pickle'):
            code = _.split('_')[0]
            __ = loadpickle(os.path.join(res_path, _))
            __['code'] = code
            pickles.append(__)

    from sqlalchemy import create_engine
    con = create_engine('mysql+pymysql://root:2021%40lskj@127.0.0.1:3306/testdb')

    for _ in pickles:
        _.to_sql('code_dtail_day', con=con, if_exists='append')

