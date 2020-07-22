#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 关于永安药业相关的数据统计

import tushare as ts
import mplfinance as mpl
import utils.ioutil as ioutil

code = '002365'

# all_date = ts.get_hist_data(code)
day_date = ts.get_tick_data(code, date='2020-07-02',src='tt')
# ioutil.save_pickle(all_date,'20200702_yayy.pickle')

# yayy_date = ioutil.load_pickle('20200702_yayy.pickle')
# print(yayy_date[:],1)
# mpl.plot(yayy_date)
print(day_date)


