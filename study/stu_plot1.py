#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tushare as ts
# import mpl_finance as mpf

wdyx = ts.get_k_data('000001','2017-01-01')

print(wdyx.head())
