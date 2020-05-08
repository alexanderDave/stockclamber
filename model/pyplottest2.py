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
from pylab import *
import datetime
import operator



#plt.xkcd()
plt.rcdefaults()

info = getDate.getDates('cn_300619')
dates = (getDate.getBody(info))['hq']
info = getDate.dealTrade(dates)

riqi = info['riqi_1']
kaipan = info['kaipanjia']
#print(kaipan)
shoupan = info['shoupanjia']

plt.figure()
ax1 = plt.subplot(211)
plt.scatter(kaipan,shoupan)

print('均值是：',np.mean(kaipan))
print('方差是：',np.var(kaipan))
print('标准差：',np.std(kaipan))
print('百分位数',np.percentile(kaipan,20))
print('三阶矩的偏度',stats.skew(kaipan))
print('四阶矩的峰度',stats.kurtosis(kaipan))

def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]
def covariance(x,y):
    n=len(x)
    return dot(de_mean(x),de_mean(y))/(n-1)
def covariance2(x,y):
    n=len(x)
    return dot(de_mean(x),de_mean(y))/(n-1)
def correlation(x,y):
    stddevx = np.std(x)
    stddevy = np.std(y)
    return covariance(x,y)/stddevx/stddevy
    
print('随机样本协方差',covariance(kaipan,shoupan))
print('整体样本协方差',covariance2(kaipan,shoupan))
print('整体样本协方差相关系数',correlation(kaipan,shoupan))
print('np corrcoef',np.corrcoef(kaipan,shoupan))

#ax2 = plt.subplot(212)
#plt.scatter(kaipan,shoupan) #绘制点图
#plt.boxplot(kaipan) #绘制箱线图
##plt.legend(['priceLine','midNum','avgNum'],loc=1) #给图画做标注
#plt.savefig('gupiao2.png',format='png')
#plt.show()

# 进行线性拟合
slope,intercept,r_value,p_value,std_err = stats.linregress(kaipan,shoupan)
print(r_value ** 2)

def predict(x):
    return [slope * t + intercept for t in x]
fitLine = predict(kaipan)
plt.scatter(kaipan,shoupan)
plt.plot(kaipan,fitLine,'g')
plt.savefig('gupiao3.png',format='png')
plt.show()









