import os

class config():

    def __init__(self):
        self.root_Path = os.path.dirname(os.path.dirname(__file__))
        self.res_path = os.path.join(self.root_Path, 'resource')
        self.plot_path = os.path.join(self.root_Path, 'plot')
        self.mysqlinfo = ('127.0.0.1', 3306, 'root', '2021@lskj')
        self.watchlist = {'300081':'HengXinDF','300364':'ZhongWenZX','600031':'SanYiZG',
                          '300014':'YiWeiLN','002007':'HuaLanSW','000625':'changanQC',
                          '601066':'ZhongXinJT','300059':'DongFCaiFu', '300999':'JingLongYu',
                          '002365':'YAYaoYe','301091':'ShenChenJiao','601888':'ZGzm',
                          '300223':'BeiJingJZ','002497':'YaHuaJiTUan','300581':'ChenXiHangKong',
                          '300088': 'ChangXinKeJi', '002409': 'YaKeKeJi','000301': 'DFshenghong',
                          }




if __name__ == '__main__':
    cf = config()
    print(cf.res_path)