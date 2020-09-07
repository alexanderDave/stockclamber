#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import utils.ioutil as ioutil
import threading
import time

class box():
    # lock = threading.RLock()

    def __init__(self):
        self.totaltime = 0

    def execute(self, n):
        # box.lock.acquire()
        self.totaltime += n
        # box.lock.release()

    def add(self):
        # box.lock.acquire()
        self.execute(1)
        # box.lock.release()

    def remove(self):
        # box.lock.acquire()
        self.execute(-1)
        # box.lock.release()

def adder(func, itme):
    while itme > 0:
        func.add()
        print('adder add 1 to box')
        itme -=1

def remover(func, itme):
    while itme > 0:
        func.remove()
        print('remover add -1 to box')
        itme -=1

def show(code):
    print(code)
    lists = df.loc[df.index == code].values.tolist()[0]
    result = list(filter(None, lists))
    return result


if __name__ == '__main__':
    savepath = '/Users/yuhandai/OneDrive/project/StockPalt/dates/dateT.pickle'
    df = ioutil.load_pickle(savepath)
    # print(df.head)
    # testdate = ['000066','000088','000089','000524','000547','000798','000818','000828','000998','002007','002030','002151','002400','002699','002905','002910','002992','300554','300850','300853','600295','600543','600590','600749','601216','603010','603551','603737','603949','605199','605318','688077','688366','688568']
    # for code in testdate:
    #     print(show(code))
    print(show('000066'))


