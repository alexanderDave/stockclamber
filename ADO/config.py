import os

class config():

    def __init__(self):
        self.root_Path = os.path.dirname(os.path.dirname(__file__))
        self.res_path = os.path.join(self.root_Path, 'resource')
        self.plot_path = os.path.join(self.root_Path, 'plot')
        self.mysqlinfo = ('127.0.0.1', 3306, 'root', '2021@lskj')
        self.watchlist = {}




if __name__ == '__main__':
    cf = config()