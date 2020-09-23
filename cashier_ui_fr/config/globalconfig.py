#coding = utf-8
'''
UI自动化框架
Date:2020-03-04
Author:刘凯
'''

'''
全局变量：各种路径
配置文件的类型：
ini,excel,yaml,py,txt

'''
import os
from public.utils.ReadConfigini import ReadConfigIni
# file_path = os.path.split(os.path.realpath(__file__))
#打印当前文件的绝对路径（globalconfig.py）'直接os获取的'
file_path = os.path.split(os.path.realpath(__file__))[0]
print(file_path)
path = os.path.join(file_path,"config.ini")
print(path)
#定义一个读取coonfig.ini文件的实例对象
read_config = ReadConfigIni(os.path.join(file_path,"config.ini"))
print(read_config)

#获取项目的绝对路径(调用实例对象的getConfigValue读取方法获取项目路径值project_paath)
project_path = read_config.getConfigValue("project","project_path")
print(project_path)
#data数据的路径
data_path = os.path.join(project_path,"Data","TestData")
print(data_path)
#report路径
report_path = os.path.join(project_path,"reports","TestReport")
print(report_path)
#TestCase_path路径
TestCase_path = os.path.join(project_path,"TestCase")
print(TestCase_path)
