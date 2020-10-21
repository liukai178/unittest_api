# 生成log的工具
# coding = utf-8
import logging
from common.handleconfig import conf
import os
from common.handlepath import *
class HandleLog(object):
    @staticmethod
    # 静态方法
    def create_logger():
        # 创建日志收集器，设置日志等级
        mylog = logging.getLogger(conf.get("log","name"))
        mylog.setLevel(conf.get("log","level"))
        #创建输出到控制台的日志等级
        sh = logging.StreamHandler()
        sh.setLevel(conf.get("log","sh_level"))
        #error级别
        mylog.addHandler(sh)
        # 丢到日志收集器中去

        #创建输出到文件的日志等级
        fh = logging.FileHandler(os.path.join(LOGDIR,"log.log"),encoding="UTF-8")
        # 输出到的文件及其目录
        fh.setLevel(conf.get("log","fh_level"))
        #设置级别（info）
        mylog.addHandler(fh)
        # 丢到日志收集器中去

        #定义输出日志的格式
        formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s:%(message)s'
        fm = logging.Formatter(formater)
        # 格式化输出
        sh.setFormatter(fm)
        fh.setFormatter(fm)

        return mylog
log = HandleLog.create_logger()
# 类直接调用静态方法
log.info("调试一下下")
# 用info级别输出”调试一下“
#输出内容：2020-06-28 22:19:18,197 - [handlelog.py-->line:29] - INFO:调试一下下