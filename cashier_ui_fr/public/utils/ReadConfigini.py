import configparser

class ReadConfigIni:
    # 默认构造函数为读取ini文件，在此前提下又封装了getConfigValue取值的方法
    #filename参数为读取的文件对象
    def __init__(self,filename):
        #类后面要写空括号，表示匿名对象
        #这个类是用来读取ini文件的
        self.cf = configparser.ConfigParser()
        # 执行读取文件（参数）的操作
        self.cf.read(filename)
    def getConfigValue(self,config,name):
        '''
        读取section和option的值
        :param config:
        :param name:
        :return:
        '''
        # 获取config下，name的值
        value = self.cf.get(config,name)
        # 取到的值要返回
        return value