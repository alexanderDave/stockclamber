import os.path

from config import config
import utiltool as tool
from DB import DB
import akshare as ak
import requests

class stockdates():

    def __init__(self, code):
        self.cf = config()
        self.code = code


    def getDaily(self, st_time, end_time):
        savepath = self.cf.res_path
        res, name = '', self.code
        dt = tool.getDates()
        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=self.code, period="daily", start_date=st_time,
                                                end_date=end_time, adjust="")
        savename = '{0}_{1}.pickle'.format(self.code, (dt[:6]).replace('-',''))
        tool.savePickle(savepath, savename, stock_zh_a_hist_df)
        with open(os.path.join(savepath, savename), 'r') as f:
            res = f.read()
        sql = f"insert into stockdata (st_name, pickledate,dt_create) values ('{name}',\"{res}\",'{dt}');"

        tool.save2db(sql)




if __name__ == '__main__':
    print('dates.py code goes here:')
    code = '000807'
    st = stockdates(code)
    st.getDaily('20200101', '20220913')