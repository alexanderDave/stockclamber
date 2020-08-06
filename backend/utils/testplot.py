#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import datetime

from matplotlib.pylab import date2num
from matplotlib.gridspec import GridSpec
from backend.utils import mplfinceplot
import utils.ioutil as ioutil

all_path = '/Users/yuhandai/OneDrive/project/StockPalt/model/__pycache__/002365_20200722.pickle'
all_day = '/Users/yuhandai/OneDrive/project/StockPalt/dates/'

# 之前扒取的单日交易详情 [{...},{...}...]格式
day_date = mplfinceplot.get_all_day_dael(all_day)
# 保存本地的所有交易信息 df格式
alldate = ioutil.load_pickle(all_path)
print(alldate)
# 获取查询日期index
date_index = []
date_day_deal = []
for _ in day_date:
    date_index.append(_['date'])
    date_day_deal.append(_['buy_sale_sum'])
date_day_deal.reverse()
# print(date_day_deal)
# date_day_sumbyday = [-328670503, -326490509, -326857890, -312162966, -314124723, -310414500, -314897557, -308794258, -329102799, -308279730, -292248480, -233127836, -251365035, -236849999, -258445669, -331345909, -308128548, -304022742, -291047382, -266704695, -273931457, -269205808, -257860592, -238543630, -240823525, -310246386, -344033138, -318911818, -326041874, -297421965, -291170398, -290160692, -253134697, -265834251, -247226251, -237191069, -213057698, -209324162, -182432916, -167196269, -153771192, -153363860, -139876708, -135196985, -134692602, -127998835, -99569890, -112563690, -96307408, -76043141, -72216319, -63172745, -61784659, -39654728, -17561771, -1187211, -4966721, -5376920, -2159891, 1041919, -5361434, 19327394, -5066406, -6172801, 3475532, 17204577, -3503628, -11804725, -5183129, -1630863, 997196, -4888455, 6930967, -2171903, -9225181, 19178578, -47621348, -30467923, -17850325, -16804576, -23650639, -18005018, -2433920, 11784904, 14819468, 1898852, -26341613, -81357609, -71688548, -103178933, -69841331, -20780669, -33253574, -3336411, -4888031, -7958348, -4755348]



# 绘制 alldate 的蜡烛图
print(alldate.columns.values.tolist())
date = alldate[['open','high','low','close','volume']]
date.rename(columns={'open':'Open','high':'High','low':'Low','close':'Close','volume':'Volume'}, inplace=True)
date.sort_index(ascending=True)
date.index = pd.DatetimeIndex(date.index)
# print(pd.to_datetime(df1['a']).values[0])

df1 = pd.DataFrame({'a':'2020-03-02'},index=[0])
new_df = date.loc[date.index >= pd.to_datetime(df1['a']).values[0]]
new_df['Volume'] = date_day_deal
# new_df['Volume'] = date_day_sumbyday
print((new_df.loc[new_df['Volume']<0])['Volume'].values.tolist())

figsize = 100,20
figure, ax = plt.subplots(figsize=figsize)
# plt.plot(date_day_sumbyday)
# plt.plot(date_day_deal)
# plt.show()
# mpf.plot(new_df,type='candle',volume=True,figratio=(3,1),figscale=15,savefig='202007263.jpg')


