#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:45:58 2019

@author: yuhandai

this is a practise for date_analyse
"""

import json,requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import operator




# init dates e.g.
#code = 'cn_600064'
#start_time = '20190101'
#end_time = '20191220'


def saveDates(code,start_time,end_time,filepath):
    baseurl = 'http://q.stock.sohu.com/hisHq?code={0}&start={1}&end={2}&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp'.format(code,start_time,end_time)
    with open('{0}/{1}.txt'.format(filepath,code),'wb') as f:
        f.write(bytes(requests.get(baseurl).text,encoding='utf8'))

    
def getDates(fileName):
    info = ''
    with open('/Volumes/D/Projects/githubsome/StockPalt/dates/{0}.txt'.format(fileName),'r') as f:
        info = f.read().strip('\n')
    return info

def getBody(mdates):
    result = {}
    
    if mdates:
        body = mdates.split('(')[1]
        info = body.split('code')
        code = (info[1].split(',')[0])[3:-1]
        status = ((info[0].split('hq')[0]).split(',')[0]).split(':')[1]
        basehq = (info[0].split('hq'))[1][3:-4].split('],')
        hqlist = []
        for hqs in basehq:
            hqlist.append((hqs.split('[')[1][1:-1]).split('","'))
        
        result['status'] = status
        result['hq'] = hqlist
        result['code'] = code
        return result
    else:
        print('dates is null')

def dealTrade(dates):
    result = {}
    
    if not dates:
        return False;
    
    mStime = []
    mTime = []
    mOpen = []
    mClose = []
    mCent = []
    mPCent = []
    mTop = []
    mButton = []
    mDeal = []
    mMone = []
    change = []
    
#数据类型说明
#   日期        开盘价  收盘价  涨跌额  涨跌幅  最低     最高     成交量   成交额     换手率
# "2019-12-13","9.31","9.41","0.18","1.95%","9.31","9.48","115162","10811.07","0.93%"
    
    for info in dates:
        mTime.append(datetime.datetime.strptime(info[0],"%Y-%m-%d"))
        mStime.append(info[0])                                      # 日期
        mOpen.append(float(info[1]))                                # 开盘价
        mClose.append(float(info[2]))                               # 收盘价
        mCent.append(float(info[3]))                                # 涨跌额
        mPCent.append(float(info[4].strip('%'))/100)                # 涨跌幅
        mButton.append(float(info[5]))                              # 最低
        mTop.append(float(info[6]))                                 # 最高
        mDeal.append(float(info[7]))                                # 成交量
        mMone.append(float(info[8])/10000)                          # 成交额
        change.append(float(info[9].strip('%'))/100)                # 换手率
    
    mTime.reverse()
    mStime.reverse()
    mOpen.reverse()
    mClose.reverse()
    mCent.reverse()
    mPCent.reverse()
    mTop.reverse()
    mButton.reverse()
    mDeal.reverse()
    mMone.reverse()
    change.reverse()
    result['riqi_1']= mTime
    result['riqi_1']= mStime
    result['kaipanjia']= mOpen
    result['shoupanjia']= mClose
    result['zhangdie']= mCent
    result['zhangdiefudu']= mPCent
    result['zuigao']= mTop
    result['zuidi']= mButton
    result['chengjiaoliang']= mDeal
    result['chengjiaoe']= mMone
    result['huanshoulv']= change
    
    
    return result

if __name__ == "__main__":
    print('code goes here:')
    # 返回的是json格式文件
    
    # 普莱柯
    #saveDates('cn_603566','20150101','20200430','/Volumes/D/Projects/githubsome/StockPalt')
    # 南京高科
    #saveDates('cn_600064','20150101','20200430','/Volumes/D/Projects/githubsome/StockPalt')
    # 金银河
    #saveDates('cn_300619','20150101','20200430','/Volumes/D/Projects/githubsome/StockPalt')
    
    
    
    info = getDates('cn_603566')
    dates = (getBody(info))['hq']
    info = dealTrade(dates)
    riqi = info['day']
    money = info['money']
    change= info['change']
    shoupan= info['shoupan']
    zhangdie = info['zhangdie']
    
    plt.plot(shoupan,'r')
    #plt.plot(money,'g')
    #plt.plot(change,'b')
    #plt.plot(zhangdie,'r')
    plt.show()
    
    min_index, min_number = min(enumerate(shoupan), key=operator.itemgetter(1))
    max_index, max_number = max(enumerate(shoupan), key=operator.itemgetter(1))
    print(min_number)
    print(max_number)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    