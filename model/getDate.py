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

#数据类型说明
#   日期        开盘价  收盘价  涨跌额  涨跌幅  最低     最高     成交量   成交额     换手率
# "2019-12-13","9.31","9.41","0.18","1.95%","9.31","9.48","115162","10811.07","0.93%"


# init dates e.g.
#code = 'cn_600064'
#start_time = '20190101'
#end_time = '20191220'


def saveDates(code,start_time,end_time,filename):
    baseurl = 'http://q.stock.sohu.com/hisHq?code={0}&start={1}&end={2}&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp'.format(code,start_time,end_time)
    with open('6000641.txt','wb') as f:
        f.write(bytes(requests.get(baseurl).text,encoding='utf8'))

    
def getDates(fileName):
    info = ''
    with open('/Volumes/D/Projects/githubsome/XhjTestPalt/{0}.txt'.format(fileName),'r') as f:
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
    
    for info in dates:
        mTime.append(datetime.datetime.strptime(info[0],"%Y-%m-%d"))
        mStime.append(info[0])
        mOpen.append(float(info[1]))
        mClose.append(float(info[2]))
        mPCent.append(float(info[4].strip('%'))/100)
        mCent.append(float(info[3]))
        mTop.append(float(info[5]))
        mButton.append(float(info[6]))
        mDeal.append(float(info[7]))
        mMone.append(float(info[8])/10000)
        change.append(float(info[9].strip('%'))/100)
        
    result['date']= mTime
    result['day']= mStime
    result['kaipan']= mOpen
    result['shoupan']= mClose
    result['zhangdie']= mCent
    result['fudu']= mPCent
    result['zuigao']= mTop
    result['zuidi']= mButton
    result['deal']= mDeal
    result['money']= mMone
    result['change']= change
    
    
    return result

if __name__ == "__main__":
    print('code goes here:')
    # 返回的是json格式文件
    info = getDates('6000641')
    dates = (getBody(info))['hq']
    info = dealTrade(dates)
    riqi = info['day']
    money = info['money']
    change= info['change']
    shoupan= info['shoupan']
    
    plt.plot(shoupan)
    plt.plot(money)
    plt.plot(change)
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    