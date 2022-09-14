import datetime
import os
import pickle
from DB import DB
import datetime

import requests


def getDates():
    ''' 获取现在的时间'''
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
    getDates()