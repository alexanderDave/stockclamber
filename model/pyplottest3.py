#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:00:46 2020

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

np.random.seed(2)
pageSpeed = np.random.normal(3.0,1.0,100)
purchAmount = np.random.normal(50.0,30.0,100) / pageSpeed

tranX = pageSpeed[:80]
testX = pageSpeed[80:]

tranY = purchAmount[:80]
testY = purchAmount[80:]

x = np.array(tranX)
y = np.array(tranY)
p4 = np.poly1d(np.polyfit(x,y,8))
xp = np.linspace(0,7,100)

plt.figure()
axe=plt.axes()
axe.set_xlim([0,7])
axe.set_ylim([0,200])
#plt.scatter(pageSpeed,purchAmount)
plt.scatter(tranX,tranY)
plt.plot(xp,p4(xp),'r')


plt.savefig('text.png',format='png')
plt.show()