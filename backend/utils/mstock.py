#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import utils.ioutil as ioutil
import tushare as ts
import io, sys, os
import pandas


class mstock(object):

    def __init__(self):
        self.mtime = time.strftime('%Y%m%d', time.localtime())
        self.mpath = ioutil.get_save_path()
        pass



    def getAllDate(self, scode):
        file_name = '{0}_{1}.pickle'.format(scode, self.mtime)
        path = os.path.join(self.mpath, file_name)
        all_date = ts.get_hist_data(scode)
        ioutil.save_pickle(all_date, path)

    # dframe 获取某一日的交易的详细数据
    def getDaydeal(self, scode, dframe):
        dates = dframe.index.values.tolist()
        for day in dates:
            # 按日获取数据并保存
            file_name = '{0}_{1}.pickle'.format(scode, day.replace('-', '_'))
            path = os.path.join(self.mpath, file_name)
            while True:
                print('开始请求:{0}'.format(file_name))
                day_date = ts.get_tick_data(scode, date=day, src='tt')
                time.sleep(1)
                if isinstance(day_date, pandas.DataFrame):
                    break
                time.sleep(5)
            ioutil.save_pickle(day_date, path)



    def test(self):
        return self.mpath

# 获取股票行业分类数据
def get_stock_type(mpath, mname):

    df = ts.get_industry_classified()
    ioutil.save_pickle(df, mpath+mname)

# 获取股票概念分类
def get_stock_classified(mpath, mname):

    df = ts.get_concept_classified()
    ioutil.save_pickle(df, mpath+mname)

# 获取股票地域分类
def get_stock_area(mpath, mname):

    df = ts.get_area_classified()
    ioutil.save_pickle(df, mpath+mname)

# 获取股票中小板分类
def get_stock_sme(mpath, mname):

    df = ts.get_sme_classified()
    ioutil.save_pickle(df, mpath+mname)

# 获取股票创业板分类
def get_stock_gme(mpath, mname):

    df = ts.get_gem_classified()
    ioutil.save_pickle(df, mpath+mname)

# 获取沪深300成份及权重
def get_stock_hs300(mpath, mname):

    df = ts.get_hs300s()
    ioutil.save_pickle(df, mpath+mname)

# 获取上证50成份股
def get_stock_sz50(mpath, mname):

    df = ts.get_sz50s()
    ioutil.save_pickle(df, mpath+mname)

# 获取中证500成份股
def get_stock_zz50(mpath, mname):

    df = ts.get_zz500s()
    ioutil.save_pickle(df, mpath+mname)

if __name__ == '__main__':
    # get yyay dates
    # mstock().getAllDate('002365')

#     /Users/yuhandai/OneDrive/project/StockPalt/dates/002365_20200722.pickle
    zz50 = '/Users/yuhandai/OneDrive/project/StockPalt/dates/zz50.pickle'
    sz50 = '/Users/yuhandai/OneDrive/project/StockPalt/dates/sz50.pickle'
    hs300 = '/Users/yuhandai/OneDrive/project/StockPalt/dates/hs300.pickle'
    cyb = '/Users/yuhandai/OneDrive/project/StockPalt/dates/cyb.pickle'
    zxb = '/Users/yuhandai/OneDrive/project/StockPalt/dates/zxb.pickle'
    area = '/Users/yuhandai/OneDrive/project/StockPalt/dates/area.pickle'
    industry = '/Users/yuhandai/OneDrive/project/StockPalt/dates/industry.pickle'
    classified = '/Users/yuhandai/OneDrive/project/StockPalt/dates/classified.pickle'

    basepath = '/Users/yuhandai/OneDrive/project/StockPalt/dates/'
    # dframe = ioutil.load_pickle(path)
    # mstock().getDaydeal('002365', dframe)
    # get_stock_type(basepath, 'industry.pickle')
    # get_stock_classified(basepath, 'classified.pickle')
    # get_stock_area(basepath, 'area.pickle')
    # get_stock_sme(basepath, 'zxb.pickle')
    # get_stock_gme(basepath, 'cyb.pickle')
    # get_stock_hs300(basepath, 'hs300.pickle')
    # get_stock_sz50(basepath, 'sz50.pickle')
    # get_stock_zz50(basepath, 'zz50.pickle')
    # df =  ioutil.load_pickle(hs300)
    df2 = ioutil.load_pickle(area)
    # print(df['name'].values)
    print(df2['name'].values.tobytes().decode(''))

