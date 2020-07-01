#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tushare as ts
import mplfinance as mpf
import matplotlib.pyplot as plt
import datetime

from matplotlib.pylab import date2num
from matplotlib.gridspec import GridSpec


def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = datetime.datetime.strptime(date,'%Y-%m-%d')
        num_date = date2num(date_time)
        num_time.append(num_date)
    return num_date




wdyx = ts.get_k_data('000001', '2017-01-01')
print(wdyx.values)
mat_wdyx = wdyx.values
num_time = date_to_num(mat_wdyx[:,0])
mat_wdyx[:,0] = num_time
Fig,(ax0,ax1) = plt.subplots(2,sharex=True,figsize=(15,8))

# ax0 = plt.subplot2grid((3,1),(0,0),rowspan=2)
# ax1 = plt.subplot2grid((3,1),(0,0))

gs = GridSpec(3,1)
plt.subplots_adjust(hspace=0.05)
ax0 = plt.subplot(gs[0:2])
ax1 = plt.subplot(gs[2])

mpf.plot(mat_wdyx)

plt.show()









