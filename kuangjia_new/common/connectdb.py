# 连接数据库
# host=None
# user=None
# password=None
# database=None
# port=None
from common.handleconfig import conf
import pymysql
class Db_Utils(object):
    def __init__(self):
        #拿到数据库的连接对象
        self.conn = pymysql.connect(host=conf.get("db","host"),
                                    user=conf.get("db","user"),
                                    password=conf.get("db","password"),
                                    database=conf.get("db","database"),
                                    port=conf.get("db","port")
                                    )
        #获取mysql数据库的游标对象
        # 1.执行sql语句
        # 2.返回结果
        self.cur = self.conn.cursor()
    def find_one(self,sql):
        # 封装查询一行数据的方法
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()
    def find_all(self,sql):
        # 封装查询表中所有数据的方法
        self.conn.commit() #提交事务
        self.cur.execute(sql)
        return self.cur.fetchall()
    def close(self):
        #关闭数据库的连接
        self.cur.close()
        self.conn.close()


