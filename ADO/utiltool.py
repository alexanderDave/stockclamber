import datetime
import os
import pickle
from DB import DB
import datetime
import pandas as pd

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

    from config import config
    import mplfinance as mpf
    respath = config().res_path
    filename = os.path.join(respath, '601601_20220.pickle')
    pk = loadpickle(filename)
    pk['日期'] = pd.to_datetime(pk['日期'])
    pk.set_index(['日期'], inplace=True)
    pk.index.set_names(['Date'], inplace=True)

    # pk.rename(columns={'开盘':'Open','收盘':'Close','最高':'High','最低':'Low'})
    column = ['Open','Close','High','Low']
    plotdate = pk.iloc[:, :4]
    plotdate.columns = column

    # upboundDC = pd.Series.index(0.0, index=pk.Close.index)
    # downboundDC = pd.Series.index(0.0, index=pk.Close.index)
    # midboundDC = pd.Series.index(0.0, index=pk.Close.index)


    # print(plotdate)

    mpf.plot(plotdate)

    # # with open(filename, 'rb') as f:
    # #     pk = (f.read()).decode('gb18030')
    #
    # dt = getDates()
    # name = 'test'
    # sql = f"insert into stockdata (st_name, pickledate, dt_create) values ('{name}',\"{pk}\" ,'{dt}');"
    # save2db(sql)