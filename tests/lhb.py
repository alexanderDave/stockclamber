#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import time
import tushare as ts
import pandas as pd
import utils.ioutil as ioutil

file_path = '/Users/yuhandai/OneDrive/project/StockPalt/stockdb/yayy.pickle'
save_path = '/Users/yuhandai/OneDrive/project/StockPalt/stockdb/longhubang'




# date
'''
参数说明：   date：日期，格式YYYY-MM-DD、retry_count：当网络异常后重试次数，默认为3、pause:重试时停顿秒数，默认为0
返回值说明： code：代码、name:名称、pchange:当日涨跌幅、amount：龙虎榜成交额(万)、buy：买入额(万)、bratio：买入占总成交比例、sell：卖出额(万)
           sratio：卖出占总成交比例、reason：上榜原因、date：日期
'''
# def getLHB(dates):
#     print(dates)
#
#     for i in dates:
#         print('goes %S' % i)
#         time = 1
#         while True:
#             date = ts.top_list(i)
#             file_name = '{0}_{1}.pickle'.format(save_path, _.replace('-', '_'))
#             if isinstance(date, pd.DataFrame):
#                 break
#             time += 1
#             if time > 5:
#                 yield print("lhb err %s " % file_name )
#                 break
#             time.sleep(2)
#         ioutil.save_pickle(date, file_name)

def get_lhb(mdate):
    print(mdate)
    while True:
        date = ts.top_list(mdate)
        file_name = '{0}_{1}.pickle'.format(save_path, mdate.replace('-', '_'))
        if isinstance(date, pd.DataFrame):
            break
        time.sleep(2)
    ioutil.save_pickle(date, file_name)



# dates = ioutil.load_pickle(file_path)
# mdatetime = dates.index.tolist()


