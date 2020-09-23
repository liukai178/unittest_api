# 路径管理
import os
# 定义项目路径
BASEDIR  = os.path.dirname(os.path.dirname(__file__))
# print(BASEDIR)

# 定义conf配置文件的路径
CONFDIR = os.path.join(BASEDIR,'config')
# print(CONFDIR)
# 定义data的路径
DATADIR = os.path.join(BASEDIR,'data')
# print(DATADIR)
# 定义logs的路径
LOGDIR = os.path.join(BASEDIR,'logs')
# print(LOGDIR)
REPORTDIR = os.path.join(BASEDIR,'reports')
# print(REPORTDIR)
CASEDIR = os.path.join(BASEDIR,'testcases')
# print(CASEDIR)
