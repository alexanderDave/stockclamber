import os.path

import mplfinance as mlp
import akshare as ak
import utiltool as tool
from config import config

def showpics():
    cf = config()
    dpath = cf.res_path
    a = tool.loadpickle(os.path.join(dpath,'000807_20220.pickle'))
    print(a)



if __name__ == '__main__':
    showpics()