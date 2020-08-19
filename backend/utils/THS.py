#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import pandas as pd
import utils.ioutil as ioutil

class THS(object):


    def __init__(self):

        pass

    def get_all_dates(self):
        header = {}
        resp = requests.get('https://eq.10jqka.com.cn/event/data/300232.txt', header=header)




if __name__ == '__main__':
    print('code test here:')
    datepath = '/Users/yuhandai/OneDrive/project/StockPalt/dates/dateT.pickle'
    savepath = '/Users/yuhandai/OneDrive/project/StockPalt/dates/dateT.xls'
    df = ioutil.load_pickle(datepath)

    # with pd.ExcelWriter(savepath) as f:
    #     df.to_excel(f, 'code', index=True)