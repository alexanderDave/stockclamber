#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy

from utils.DateUtils import stockDate


class Dateanly():

    def __init__(self):

        pass

    @staticmethod
    def getAvg(dates):
        sizes = []
        for dd in dates['hq']:
            sizes.append(abs(float(dd[3])))
        avg_sizes = numpy.average(sizes)

        return avg_sizes



if __name__ == '__main__':
    yayy = stockDate.readDate('cn_002365')
    zmkj = stockDate.readDate('cn_300232')
    njgk = stockDate.readDate('cn_600064')
    jyh = stockDate.readDate('cn_300619')
    plk = stockDate.readDate('cn_603566')

    print(Dateanly.getAvg(yayy))
    print(Dateanly.getAvg(zmkj))
    print(Dateanly.getAvg(njgk))
    print(Dateanly.getAvg(jyh))
    print(Dateanly.getAvg(plk))
