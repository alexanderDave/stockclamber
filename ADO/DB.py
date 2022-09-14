# -*- coding: UTF-8 -*-
import pymysql
from config import config

class DB(object):
    """
    封装了数据库基本操作，用法如下：
    testdb = DB(mdatabase=None)             #实例化db类
    testdb.connDb()                         #创建conn连接，参数说明见func注释
    print(testdb.select_one('select * from green_credit_active_person limit 1;')) #执行增改查操作
    testdb.closeDb()                        #释放连接

    """

    def __init__(self, mdatabase=None):
        self.cf = config()
        self.mdate = mdatabase
        self.conn = None

    def connDb(self):
        """
        :param evn: 切换连接数据的环境 ['beta':beta环境数据库，其他都连接到测试环境数据库]
        :param mdatabase: 连接的数据库，不输入则连接到config文件默认的数据库
        :return: 返回数据连接conn
        """

        mdatabase = 'test' if None == self.mdate else self.mdate
        try:
            self.conn = pymysql.connect(host=self.cf.mysqlinfo[0],
                                        port=self.cf.mysqlinfo[1],
                                        user=self.cf.mysqlinfo[2],
                                        password=self.cf.mysqlinfo[3],
                                        database=mdatabase, charset='utf8')
            # print('db conned !')
        except Exception as identifier:
            print(identifier)
            return identifier

    def closeDb(self):
        if None != self.conn:
            self.conn.close()
        # print('db closed!')
        return True

    def getCursor(self):
        if None != self.conn:
            return self.conn.cursor()

    # insert
    def insert(self, sql, *value):
        if None != self.conn:
            num = self.getCursor().execute(sql, *value)
            self.conn.commit()
            return num

    # select
    def select_one(self, sql, *value):
        if None != self.conn:
            corsor = self.getCursor()
            corsor.execute(sql, *value)
            result = corsor.fetchone()
            self.conn.commit()
            return result

    def select_all(self, sql):
        if None != self.conn:
            corsor = self.getCursor()
            corsor.execute(sql)
            result = corsor.fetchall()
            self.conn.commit()
            return result

    # update
    def update(self, sql, *value):
        if None != self.conn:
            n = self.getCursor().execute(sql, *value)
            self.conn.commit()
            return n


if __name__ == "__main__":
    print('test env db code goes here:')
    # sql = 'select `asset_id` from asset where `status`=0 order by id desc limit 1;'
    #
    # testdb = DB('testdb')
    # testdb.connDb()
    # name = 'test'
    # sql = f"insert into stockdata (st_name, dt_create) values ('{name}','2022-09-14');"
    # print(sql)
    # result = testdb.update(sql)
    # # print(result[0][0])
    # testdb.closeDb()




