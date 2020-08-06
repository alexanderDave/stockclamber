#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import utils.ioutil as ioutil
import tushare as ts
import io, sys, os
import pandas


class mstock(object):

    def __init__(self):
        self.mtime = time.strftime('%Y%m%d', time.localtime())
        self.mpath = ioutil.get_save_path()
        pass



    def getAllDate(self, scode):
        file_name = '{0}_{1}.pickle'.format(scode, self.mtime)
        path = os.path.join(self.mpath, file_name)
        all_date = ts.get_hist_data(scode)
        ioutil.save_pickle(all_date, path)

    # dframe 获取某一日的交易的详细数据
    def getDaydeal(self, scode, dframe):
        dates = dframe.index.values.tolist()
        for day in dates:
            # 按日获取数据并保存
            file_name = '{0}_{1}.pickle'.format(scode, day.replace('-', '_'))
            path = os.path.join(self.mpath, file_name)
            while True:
                print('开始请求:{0}'.format(file_name))
                day_date = ts.get_tick_data(scode, date=day, src='tt')
                time.sleep(1)
                if isinstance(day_date, pandas.DataFrame):
                    break
                time.sleep(5)
            ioutil.save_pickle(day_date, path)



    def test(self):
        return self.mpath


if __name__ == '__main__':
    # get yyay dates
    # mstock().getAllDate('002365')

#     /Users/yuhandai/OneDrive/project/StockPalt/dates/002365_20200722.pickle
    path = '/Users/yuhandai/OneDrive/project/StockPalt/model/__pycache__/002365_20200722.pickle'
    dframe = ioutil.load_pickle(path)
    mstock().getDaydeal('002365', dframe)

'''
import tushare as ts
import mplfinance as mpl
import utils.ioutil as ioutil

code = '002365'

# 

# ioutil.save_pickle(all_date,'20200702_yayy.pickle')

# yayy_date = ioutil.load_pickle('20200702_yayy.pickle')
# print(yayy_date[:],1)
# mpl.plot(yayy_date)
print(day_date)'''