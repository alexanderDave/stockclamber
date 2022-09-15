import os

class config():

    def __init__(self):
        self.root_Path = os.path.dirname(os.path.dirname(__file__))
        self.res_path = os.path.join(self.root_Path, 'resource')
        self.plot_path = os.path.join(self.root_Path, 'plot')
        self.mysqlinfo = ('127.0.0.1', 3306, 'root', '2021@lskj')
        self.watchlist = {'300081':'恒信东方','300364':'中文在线','600031':'三一重工','300014':'亿纬锂能',
                          '601601':'中国太保','601066':'中信建投','300059':'东方财富',
                          '300999':'金龙鱼','002007':'华兰生物','002833':'宏亚数控',
                          '300058':'蓝色光标','301091':'深城交','300031':'宝通科技',
                          '300223':'北京君正','002497':'雅化集团','300581':'晨曦航空',
                          '300045': '华力创通', '300088': '长信科技', '002409': '雅克科技',
                          }




if __name__ == '__main__':
    cf = config()