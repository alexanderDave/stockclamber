#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests


class THS(object):


    def __init__(self):

        pass

    def get_all_dates(self):
        header = {}
        resp = requests.get('https://eq.10jqka.com.cn/event/data/300232.txt', header=header)




if __name__ == '__main__':
    print('code test here:')