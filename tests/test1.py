#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:45:58 2019

@author: yuhandai

this is a practise for date_analyse
"""
import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}


'''http://q.stock.sohu.com/hisHq
?code=zs_000001&start=20000504&end=20151215&stat=1&order=D&period=d&
callback=historySearchHandler&rt=jsonp&r=0.8391495715053367&0.9677250558488026'''


#murl = r'http://q.stock.sohu.com/hisHq?code=zs_000001&start=20000504&end=20151215&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp&r=0.8391495715053367&0.9677250558488026'

code = 'cn_600064'
start_time = '20190101'
end_time = '20191220'
baseurl = 'http://q.stock.sohu.com/hisHq?code={0}&start={1}&end={2}&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp'.format(code,start_time,end_time)

def getHq():
    dates = requests.get(baseurl).text
    result = {}
    if dates:
        body = dates.split('(')[1]
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
        print(result['hq'])
        return result
    else:
        print('dates is null')



if __name__ == "__main__":
    print('code goes here:')
    with open('6000641.txt','wb') as f:
        f.write(bytes(requests.get(baseurl).text,encoding='utf8'))
    print(requests.get(baseurl).text)
    # getHq()
