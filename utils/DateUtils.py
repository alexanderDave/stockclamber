#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,time
import requests
import pickle
import numpy
import json
#数据类型说明
#   日期        开盘价  收盘价  涨跌额  涨跌幅  最低     最高     成交量   成交额     换手率
# "2019-12-13","9.31","9.41","0.18","1.95%","9.31","9.48","115162","10811.07","0.93%"

class stockDate():


    def __init__(self,stock,startime,endtime):
        self.stock = stock
        self.startime = startime
        self.endtime = endtime


    def savedate(self):
        # save_path: ../dates/xxx.pick
        save_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'dates')
        baseurl = 'http://q.stock.sohu.com/hisHq?code={0}&start={1}&end={2}&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp'.format(
            self.stock, self.startime, self.endtime)
        resp = requests.get(baseurl)
        resp_date = self.getBody(resp.text)
        with open('{0}/{1}.pickle'.format(save_path,self.stock),'wb') as f:
            pickle.dump(resp_date,f)

        return True



    @staticmethod
    def readDate(dates):
        save_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'dates')
        with open('{0}/{1}.pickle'.format(save_path, dates), 'rb') as f:
            result = pickle.load(f)

            return result

        return False

    @staticmethod
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


if __name__ == '__main__':
    # 存储待分析数据
    print('test here')
    # cn_002365 = stockDate('cn_002365', '20180101', '20200608')
    # cn_300232 = stockDate('cn_300232', '20180101', '20200608')
    # cn_600064 = stockDate('cn_600064', '20180101', '20200608')
    # cn_300619 = stockDate('cn_300619', '20180101', '20200608')
    # cn_603566 = stockDate('cn_603566', '20180101', '20200608')
    #
    #
    # cn_600064.savedate()
    # cn_002365.savedate()
    # cn_300232.savedate()
    # cn_300619.savedate()
    # cn_603566.savedate()

    # yayy = stockDate.readDate('cn_002365')
    # zmkj = stockDate.readDate('cn_300232')
    # njgk = stockDate.readDate('cn_600064')
    # jyh = stockDate.readDate('cn_300619')
    # plk = stockDate.readDate('cn_603566')
    # print(len(a['hq']))   # 569

