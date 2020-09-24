


import configparser

from common.handlepath import *
from common.ddt import ddt,data
from common.handleconfig import *
from common.handleconfig import HandleConfig
from common.readexcel import *
from common.handlerequests import *
from common.handlelog import log
import warnings
from configparser import ConfigParser
import json
import requests
filename = os.path.join(CONFDIR,'config.ini')
def get_token():
    # warnings.simplefilter("ignore", ResourceWarning)
    url = conf.get("env", "url") + '/login'
    # print(url)
    data = {'mobile': conf.get('test-data', 'mobile'),
            'password': conf.get('test-data', 'password')}
    # headers = conf.get('env', 'headers')
    # 第二步：发送接口请求是为了让登录接口和登录后的接口保持会话

    response = requests.request(method="post",url=url,data=data)
    res = response.json()
    # print(res)
    token = res['data']['token']
    result_1 = {"Content-Type": "application/json", "token": token}
    # print(result_1)
    # 重新拼接最新的token并写入配置文件
    config = configparser.ConfigParser()
    config.read(filename)
    config.set("env", "headers", str(result_1))
    config.write(open(filename, "w"))
    # print(headers)
# get_token()
