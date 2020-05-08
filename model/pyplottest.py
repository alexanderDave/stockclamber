#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:02:37 2020

@author: yuhandai
"""

import json,requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import datetime
import operator
import getDate


#plt.xkcd()
plt.rcdefaults()

info = getDate.getDates('cn_603566')
dates = (getDate.getBody(info))['hq']
info = getDate.dealTrade(dates)

riqi = info['riqi_1']
kaipan = info['kaipanjia']
#print(kaipan)
shoupan = info['shoupanjia']

plt.figure()
#绘制当前数据离散化后的直方图，分析数据的分布范围
ax2 = plt.subplot(212)
plt.hist(kaipan,120)
#绘制当前数据离散化后的直方图，分析数据的分布范围
ax1 = plt.subplot(211)
plt.plot(kaipan,'r')


#中位数
middu = np.median(kaipan)
print('中位数是：',middu)
plt.hlines(middu,1,len(kaipan),'b')
#重数

print('重数是：',stats.mode(kaipan))
#plt.hlines(avgKai,1,len(kaipan),'g')
#平均数
avgnu = np.mean(kaipan)
print('平均数是：',avgnu)
plt.hlines(avgnu,1,len(kaipan),'g')
plt.legend(['priceLine','midNum','avgNum'],loc=1)
plt.savefig('gupiao.png',format='png')
plt.show()
