#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import tushare as ts
import pandas as pd
import utils.ioutil as ioutil

def getcode(code):
    print(code)
    lists = df.loc[df.index == code].values.tolist()[0]
    result = list(filter(None, lists))
    return result

loadpath = '/Users/yuhandai/OneDrive/project/StockPalt/dates/lhb20200904.pickle'
savepath = '/Users/yuhandai/OneDrive/project/StockPalt/dates/'

df = ioutil.load_pickle(loadpath)

# 获取df的时间列表，日期由近及远
timelist = df.index.tolist()
list.sort(timelist, reverse=True)

print(len(timelist))

# 将df[[date:stocklist],[date:stocklist]...] 格式转换成
stock_pool = [] # 已经跑过数据的stock列表
result = {}
for ti in timelist:
    # codelist：每天上榜的股票
    codelist = list(filter(None, df.loc[df.index == ti].values.tolist()[0]))
    # 剩下需要跑的日期list
    restDate = timelist[timelist.index(ti)+1:]

    print(stock_pool)
    codehistory = []
    for code in codelist:
        # 跑过的数据不再跑
        if code in stock_pool:
            print('out:', code)
            continue
        if code == None:
            continue
        # histroydate = ts.get_hist_data(code)
        # ioutil.save_pickle(histroydate, savepath+code+'.pickle')
        # 记录该股票在龙虎榜里出现的数据
        # print(code)
        codehistory.append(ti)
        stock_pool.append(code)
        for _date in restDate:
            # print('\t\t\t\t第{0}天的数据开始循环{1}往后的'.format(ti, _date))
            restcode = list(filter(None, df.loc[df.index == _date].values.tolist()[0]))
            # print('{0}:code:{1}is runing--{2}::{3}'.format(ti, code, _date, restcode))
            # print('restcode:', restcode)
            if code in restcode:
                codehistory.append(_date)
        finalist = list(set(codehistory))

        result[code] = finalist

        # 已经跑过数据的增加记录


mdf = pd.DataFrame.from_dict(result, orient='index')
ioutil.save_pickle(mdf, savepath+'dateT.pickle')
# df1.to_excel(f, 'code', index=True)




