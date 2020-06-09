#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:00:34 2020

@author: yuhandai
"""
import json,requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import datetime

info = getDate.getDates('cn_603566')
dates = (getDate.getBody(info))['hq']
info = getDate.dealTrade(dates)

riqi = info['riqi_1']
kaipan = info['kaipanjia']
#print(kaipan)
shoupan = info['shoupanjia']
zuigao = info['zuigao']
zuidi = info['zuidi']

plt.figure()
ax1 = plt.subplot(211)
plt.scatter(zuidi,zuigao)

slope,intercept,r_value,p_value,std_err = stats.linregress(zuidi,zuigao)
print(r_value ** 2)
print('fitline is {0}x+{1}'.format(slope,intercept))

def predict(x):
    return [slope * t + intercept for t in x]
fitLine = predict(zuidi)
ax2 = plt.subplot(212)
plt.plot(zuidi,fitLine,'g')
plt.show()