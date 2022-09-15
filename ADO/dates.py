import os.path

from config import config
import utiltool as tool
from DB import DB
import akshare as ak
import requests
from qiyechatutil import Weichat
import mplfinance as mpf

class stockdates():

    def __init__(self, code):
        self.cf = config()
        self.code = code


    def getDaily(self, st_time, end_time):
        savepath = self.cf.res_path
        res, name = '', self.code
        dt = tool.getDatenow()
        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=self.code, period="daily", start_date=st_time,
                                                end_date=end_time, adjust="")
        savename = '{0}_{1}.pickle'.format(self.code, dt)
        tool.savePickle(savepath, savename, stock_zh_a_hist_df)
        with open(os.path.join(savepath, savename), 'r') as f:
            res = f.read()
        sql = f"insert into stockdata (st_name, pickledate,dt_create) values ('{name}',\"{res}\",'{dt}');"

        tool.save2db(sql)

    def genFinance(self):
        respath = config().res_path
        filename = os.path.join(respath, '601601_20220.pickle')
        pk = loadpickle(filename)
        pk['日期'] = pd.to_datetime(pk['日期'])
        pk.set_index(['日期'], inplace=True)
        pk.index.set_names(['Date'], inplace=True)

        pk.rename(columns={'开盘': 'Open', '收盘': 'Close', '最高': 'High', '最低': 'Low'}, inplace=True)
        pk = pk.iloc[:, :4]
        print(pk)
        upboundDC = pd.Series(0.0, index=pk.Close.index)
        downboundDC = pd.Series(0.0, index=pk.Close.index)
        midboundDC = pd.Series(0.0, index=pk.Close.index)
        rate = 0.4
        for _ in range(20, len(pk.Close)):
            upboundDC[_] = max(pk.High[(_ - 20):_])
            downboundDC[_] = min(pk.Low[(_ - 20):_])
            # midboundDC[_] = 0.382 * (upboundDC[_] + downboundDC[_])
            midboundDC[_] = (upboundDC[_] - downboundDC[_]) * rate + downboundDC[_]

        pk['upboundDC'] = upboundDC
        pk['downboundDC'] = downboundDC
        pk['midboundDC'] = midboundDC
        plotdate = pk.iloc[-60:, :]

        add_plot = [mpf.make_addplot(plotdate['upboundDC']),
                    mpf.make_addplot(plotdate['downboundDC']),
                    mpf.make_addplot(plotdate['midboundDC'])]

        picname = filename.replace('pickle', 'png')
        mpf.plot(plotdate, type='candle', addplot=add_plot, savefig=picname, title='demotest', mav=5)
        Weichat().sendPics(picname)




if __name__ == '__main__':
    print('dates.py code goes here:')
    code = '000807'
    st = stockdates(code)
    st.getDaily('20200101', '20220913')