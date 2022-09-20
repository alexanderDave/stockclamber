import os.path
import time

from config import config
import utiltool as tool
from DB import DB
import akshare as ak
import requests
from qiyechatutil import Weichat
import mplfinance as mpf
import pandas as pd

class stockdates():

    def __init__(self, code, name):
        self.cf = config()
        self.code = code
        self.name = name
        self.path = ''


    def getDaily(self, duration):
        end_time = tool.getDatenow()
        st_time = tool.getDatenow(duration)
        savepath = self.cf.res_path
        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=self.code, period="daily", start_date=st_time,
                                                end_date=end_time, adjust="")
        self.path = '{0}_{1}.pickle'.format(self.code, end_time)
        tool.savePickle(savepath, self.path, stock_zh_a_hist_df)
        # with open(os.path.join(savepath, self.path), 'r') as f:
        #     res = f.read()
        # sql = f"insert into stockdata (st_name, pickledate,dt_create) values ('{name}',\"{res}\",'{dt}');"
        # tool.save2db(sql)

    def genFinance(self, rates=None, duration=None, mavs=None,tongdao=None):
        respath = self.cf.res_path
        filename = os.path.join(respath, self.path)
        pk = tool.loadpickle(filename)
        pk['日期'] = pd.to_datetime(pk['日期'])
        pk.set_index(['日期'], inplace=True)
        pk.index.set_names(['Date'], inplace=True)

        pk.rename(columns={'开盘': 'Open', '收盘': 'Close', '最高': 'High', '最低': 'Low'}, inplace=True)
        pk = pk.iloc[:, :4]
        # print(pk)
        upboundDC = pd.Series(0.0, index=pk.Close.index)
        downboundDC = pd.Series(0.0, index=pk.Close.index)
        midboundDC = pd.Series(0.0, index=pk.Close.index)
        rate = 0.4 if None == rates else rates
        size = 20 if None == tongdao else tongdao
        for _ in range(size, len(pk.Close)):
            upboundDC[_] = max(pk.High[(_ - size):_])
            downboundDC[_] = min(pk.Low[(_ - size):_])
            midboundDC[_] = (upboundDC[_] - downboundDC[_]) * rate + downboundDC[_]

        pk['upboundDC'] = upboundDC
        pk['downboundDC'] = downboundDC
        pk['midboundDC'] = midboundDC
        les = -60 if None == duration else duration
        plotdate = pk.iloc[les:, :]

        add_plot = [mpf.make_addplot(plotdate['upboundDC']),
                    mpf.make_addplot(plotdate['downboundDC']),
                    mpf.make_addplot(plotdate['midboundDC'])]

        picname = filename.replace('pickle', 'png')
        m = 10 if None == mavs else mavs
        mpf.plot(plotdate, type='candle', addplot=add_plot, savefig=picname, title=self.name, mav=m)
        time.sleep(8)
        Weichat().sendPics(picname)
        Weichat().sendTxt('{0}:{1}'.format(self.name, plotdate.loc[pk.index[-1]].values[:]))




if __name__ == '__main__':
    print('dates.py code goes here:')
