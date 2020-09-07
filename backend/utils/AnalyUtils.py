#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import utils.ioutil as ioutil

from utils.DateUtils import stockDate


class Dateanly():

    def __init__(self,name):
        self.date = stockDate.readDate(name)

        pass

    def getDateAvg(self):
        return self.getAvg(self.date)

    @staticmethod
    def getAvg(dates):
        sizes = []
        for dd in dates['hq']:
            sizes.append(abs(float(dd[3])))
        avg_sizes = numpy.average(sizes)

        return avg_sizes


if __name__ == '__main__':
    t = '/Users/yuhandai/OneDrive/project/StockPalt/dates/dateT.pickle'
    df = ioutil.load_pickle(t)
    print(df.loc[df.index == '300009'].values.tolist()[0])

    pass



