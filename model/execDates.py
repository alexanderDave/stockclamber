#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:32:07 2020

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
import getDate

plt.figure(figsize=(50, 50))
info = getDate.getDates('cn_603566')
dates = (getDate.getBody(info))['hq']
info = getDate.dealTrade(dates)
print(info['chengjiaoliang'])
print(len(info['chengjiaoliang']))

#shoupan = map(lambda x:x*1000,info['shoupanjia'])

x = np.linspace(1,1184,1184)
y = info['chengjiaoliang']
#y1 = shoupan
plt.plot(x,y)
#plt.plot(x,y1)
plt.savefig('1.png')
