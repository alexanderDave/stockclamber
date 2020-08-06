#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import tushare as ts
import time,os,datetime
import requests
import pickle
import numpy as np
import pandas as pd
import utils.ioutil as ioutil


file_path = '/Users/yuhandai/OneDrive/project/StockPalt/dates/'

def sum_arry_list(mlist):
    result = 0
    for x in mlist:
        result += x
    return result


def get_all_deal(df):
    result = {}
    testdate = df.copy(deep=True)
    testdate.loc[testdate.type == '卖盘', 'type'] = -1
    testdate.loc[testdate.type == '买盘', 'type'] =  1
    testdate.loc[testdate.type == '中性盘', 'type'] = 1
    testdate['new'] = testdate['amount'].mul(testdate['type'])
    amount1 = testdate['amount'].values
    amount2 = testdate['new'].values

    result['all_deal'] = sum_arry_list(amount1)
    result['buy_sale_sum'] = sum_arry_list(amount2)

    return result

# return [{
#           'date':交易日期 2020-01-01,'all_deal':当日成交总金额,'buy_sale_sum':买卖金额差额,},
#           {...}...]
#
def get_all_day_dael(path):
    files = list(map(lambda x: os.path.join(path, x), os.listdir(path)))
    lists = []
    for file in files:
        if file.__contains__('DS_Store'):
            # print(file)
            continue
        date = datetime.datetime.strptime((file[-17:-7]).replace('_', '-'), '%Y-%m-%d')
        day_deal = ioutil.load_pickle(file)
        info = get_all_deal(day_deal)
        info['date'] = date
        lists.append(info)
    lists.sort(key=lambda x: x['date'],reverse=False)

    return lists

if __name__ == '__main__':
    print('test here')

    # files = os.listdir(file_path) # 列出当前目录下的所有的文件
    lists = get_all_day_dael(file_path)
    for x in lists:
        print('%s|%s||%s' % (x['date'], x['all_deal'], x['buy_sale_sum']))






