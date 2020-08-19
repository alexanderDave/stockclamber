#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import time,os
import tushare as ts
import pandas as pd
import utils.ioutil as ioutil


lhb_path = '/Users/yuhandai/OneDrive/project/StockPalt/dates/lhb/'
excel = '/Users/yuhandai/OneDrive/project/StockPalt/dates/lnb.xls'



# date
'''
参数说明：   date：日期，格式YYYY-MM-DD、retry_count：当网络异常后重试次数，默认为3、pause:重试时停顿秒数，默认为0
返回值说明： code：代码、name:名称、pchange:当日涨跌幅、amount：龙虎榜成交额(万)、buy：买入额(万)、bratio：买入占总成交比例、sell：卖出额(万)
           sratio：卖出占总成交比例、reason：上榜原因、date：日期
'''
# def getLHB(dates):
#     print(dates)
#
#     for i in dates:
#         print('goes %S' % i)
#         time = 1
#         while True:
#             date = ts.top_list(i)
#             file_name = '{0}_{1}.pickle'.format(save_path, _.replace('-', '_'))
#             if isinstance(date, pd.DataFrame):
#                 break
#             time += 1
#             if time > 5:
#                 yield print("lhb err %s " % file_name )
#                 break
#             time.sleep(2)
#         ioutil.save_pickle(date, file_name)

def get_lhb(mdate):
    print(mdate)
    while True:
        date = ts.top_list(mdate)
        file_name = '{0}longhubang_{1}.pickle'.format(lhb_path, mdate.replace('-', '_'))
        if isinstance(date, pd.DataFrame):
            break
        time.sleep(2)
    ioutil.save_pickle(date, file_name)

def save_to_excel():
    files = os.listdir(lhb_path)

    with pd.ExcelWriter(excel) as fi:
        for f in files:
            if f.__contains__('DS_Store'):
                continue
            filepath = os.path.join(lhb_path, f)
            dates = ioutil.load_pickle(filepath)
            savename = f[11:-7]
            print('saveing %s '% filepath)
            dates.to_excel(fi, savename, index=False)
        print('over!')

def deal_lhb():

    lhbv2_path = '/Users/yuhandai/OneDrive/project/StockPalt/dates/lhbv2/'
    names = os.listdir(lhb_path)
    for name in names:
        if name.__contains__('DS_Store'):
            continue
        date_path = os.path.join(lhb_path,name)
        save_path = os.path.join(lhbv2_path,name)
        print(date_path)
        df = ioutil.load_pickle(date_path)
        df = df.drop(df[df['name'].str.contains('ST|退市|退') == True].index)
        df = df.drop_duplicates('code', keep='first', inplace=False)
        print(save_path)
        ioutil.save_pickle(df, save_path)
    print('over')


    # excel = '/Users/yuhandai/OneDrive/project/StockPalt/dates/test1.xls'
    # with pd.ExcelWriter(excel) as fi:
    #     test_path = '/Users/yuhandai/OneDrive/project/StockPalt/dates/lhb/longhubang_2020_08_06.pickle'  # size:19210
    #     df = ioutil.load_pickle(test_path)
    #     df.to_excel(fi, 'before', index=False)
    #     # df = df.drop(df[(df['name'].contains('ST')) | (df['name'].contains('退市'))].index)
    #     df = df.drop(df[df['name'].str.contains('ST|退市|退') == True].index)
    #     # df = df.drop(df.name.__contains__('ST') or df.name.__contains__('退'),axis = 0)
    #     df = df.drop_duplicates('code', keep='first', inplace=False)
    #     df.to_excel(fi, 'after', index=False)



def getdetial(mpath):
    date = ioutil.load_pickle(mpath)
    date['pchange'] = date['pchange'].astype('float')
    # date['sell'] = date['sell'].astype('float')
    df = date[date['pchange'] > 0 ]
    excel = '/Users/yuhandai/OneDrive/project/StockPalt/dates/test2.xls'
    with pd.ExcelWriter(excel) as fi:
        df.to_excel(fi, 'after', index=False)
        date.to_excel(fi, 'before', index=False)


    # print(df)


def save_excel_by_date(tname):
    basepath = '/Users/yuhandai/OneDrive/project/StockPalt/dates/lhb{0}.pickle'.format(tname)
    lhbv2_path = '/Users/yuhandai/OneDrive/project/StockPalt/dates/lhb/'
    excel = '/Users/yuhandai/OneDrive/project/StockPalt/dates/lhb{0}.xls'.format(tname)
    filename = os.listdir(lhbv2_path)
    with pd.ExcelWriter(excel) as f:
        date1 = {}
        date2 = {}
        for fi in filename:
            if fi.__contains__('DS_Store'):
                continue
            title = fi[11:-7].replace('_', '')
            dpath = os.path.join(lhbv2_path, fi)
            dd = ioutil.load_pickle(dpath)
            dd = dd.drop(dd[dd['name'].str.contains('ST|退市|退') == True].index)
            dd = dd.drop_duplicates('code', keep='first', inplace=False)
            dd['nline'] = dd['name'] + dd['pchange']

            # 判断买入buy-sell > 0
            dd['buy'] = dd['buy'].apply(lambda x: float(x) if x != '' else 0)
            dd['sell'] = dd['sell'].apply(lambda x: float(x) if x != '' else 0)
            dd['ot'] = dd['buy'] - dd['sell']
            dd = dd.drop(dd[dd['ot'] < 0].index)

            code = dd['code'].values.tolist()
            name = dd['nline'].values.tolist()
            date1[title] = code
            date2[title] = name
        # print(date1)
        # print(date2)
        df1 = pd.DataFrame.from_dict(date1, orient='index')
        df2 = pd.DataFrame.from_dict(date2, orient='index')
        # ioutil.save_pickle(df1, '/Users/yuhandai/OneDrive/project/StockPalt/dates/lhb20200819.pickle')
        df1.to_excel(f, 'code', index=True)
        df2.to_excel(f, 'name', index=True)

def get_daily_date():
    now = time.strftime('%Y-%m-%d')
    get_lhb(now)

# getdetial('/Users/yuhandai/OneDrive/project/StockPalt/dates/lhbv2/longhubang_2020_08_06.pickle')

dt = time.strftime('%Y%m%d')
get_daily_date()
save_excel_by_date(dt)








