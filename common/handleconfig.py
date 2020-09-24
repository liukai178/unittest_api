# 读取配置文件的工具(conf)
from configparser import ConfigParser
from common.handlepath import *
import os
# from common.gettoken import *

#通过section，option获取value的类
class HandleConfig(ConfigParser):
    def __init__(self,filename):
        super().__init__(self)
        # 继承父类的构造函数
        self.filename = filename
        self.read(filename)

    def write_data(self,section, option, value=None):
        self.set(section, option, value)
        # 通过set写入内容
        self.write(fp=open(self.filename))
        # 写入哪个文件
# conf = HandleConfig(os.path.join(CONFDIR,'config.ini'))
conf = HandleConfig(os.path.join(CONFDIR,"config.ini"))
# print(conf.get('log', 'name'))
# print(conf.get('db','host'))
# a =  HandleConfig(conf)
# a.write_data('env','headers',token)