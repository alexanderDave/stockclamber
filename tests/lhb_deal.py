#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#


import utils.ioutil as ioutil

loadpath = '/Users/yuhandai/OneDrive/project/StockPalt/dates/lhb20200814.pickle'
df = ioutil.load_pickle(loadpath)

# 获取df的时间列表，日期由近及远
timelist = df.index.tolist()
list.sort(timelist, reverse=True)

# print(timelist)

# 将df[[date:stocklist],[date:stocklist]...] 格式转换成
stock_pool = [] # 已经跑过数据的stock列表
for ti in timelist:
    restlist = timelist[timelist.index(ti)+1:]
    codelist = df.loc[df.index == ti].valuesl.tolist()

    pass

