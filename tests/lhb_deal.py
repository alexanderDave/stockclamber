#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import tushare as ts
import pandas as pd
import utils.ioutil as ioutil

loadpath = '/Users/yuhandai/OneDrive/project/StockPalt/dates/lhb20200814.pickle'
savepath = '/Users/yuhandai/OneDrive/project/StockPalt/dates/'

df = ioutil.load_pickle(loadpath)

# 获取df的时间列表，日期由近及远
timelist = df.index.tolist()
list.sort(timelist, reverse=True)

# print(timelist)

# 将df[[date:stocklist],[date:stocklist]...] 格式转换成
stock_pool = [] # 已经跑过数据的stock列表
result = {}
for ti in timelist:
    restlist = timelist[timelist.index(ti)+1:]
    codelist = df.loc[df.index == ti].values.tolist()[0]
    print(codelist)
    codehistory = []
    for code in codelist:
        # 跑过的数据不再跑
        if code in stock_pool:
            continue
        if code == None:
            continue
        # histroydate = ts.get_hist_data(code)
        # ioutil.save_pickle(histroydate, savepath+code+'.pickle')
        # 记录该股票在龙虎榜里出现的数据
        # print(code)
        for rest in restlist:
            restcode = df.loc[df.index == rest].values.tolist()[0]
            print('restcode:', restcode)
            if code in restcode:
                codehistory.append(rest)
        result[code] = codehistory

        # 已经跑过数据的增加记录
        stock_pool.append(code)

mdf = pd.DataFrame.from_dict(result, orient='index')
ioutil.save_pickle(mdf, savepath+'dateT.pickle')
# df1.to_excel(f, 'code', index=True)




