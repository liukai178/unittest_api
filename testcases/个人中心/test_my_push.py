import os
import unittest

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
from common.Get_token import get_token
case_file = os.path.join(DATADIR,"apicase.xlsx")
filename = os.path.join(CONFDIR,'config.ini')
print(filename)
@ddt
class Test_My_Push(unittest.TestCase):
    excel = ReadExcel(case_file,"my_push")
    cases = excel.read_data()
    request = SendRequests()
    @classmethod
    def setUpClass(cls):
        # # 忽略这个报错
        warnings.simplefilter("ignore", ResourceWarning)
        # get_token()
        #第一步：准备接口请求的数据
        url = conf.get("env","url") + '/login'
        print(url)
        data = {'mobile':conf.get('test-data','mobile'),
                'password':conf.get('test-data','password')}
        headers = conf.get('env','headers')
        #第二步：发送接口请求是为了让登录接口和登录后的接口保持会话

        response = cls.request.send(method='post',url=url,data=data,headers=headers)
        res = response.json()
        print(res)
        token = res['data']['token']
        result_1 = {"Content-Type":"application/json","token":token}
        print(result_1)
        # 重新拼接最新的token并写入配置文件
        config = configparser.ConfigParser()
        config.read(filename)
        config.set("env", "headers", str(result_1))
        config.write(open(filename, "w"))

    @data(*cases)
    def test001_my_push(self,case):
        url = conf.get("env", "url") + case["url"]
        # print(url)
        method = case['method']
        # print(method)
        data = eval(case['data'])
        # eval这个内置函数的作用：执行一个字符串表达式，并且返回执行后的结果
        headers = eval(conf.get("env","headers"))
        # print(headers)
        # 从配置文件文件config.ini中取header等常用请求头信息或者接口参数
        expected = eval(case['expected'])
        # print(expected)
        # 从excel取expected预期结果内容
        row = case['case_id'] + 1
        # 每跑一行，case_id + 1

        # 第二步，发送接口请求
        response = self.request.send(method=method, url=url, headers=headers,data=data)
        print(response.text)
        result = response.json()
        print(result)


        # 第三步：接口的断言
        try:  # 期待值和实际结果值对比断言
            self.assertEqual(expected['code'], result['code'])
            self.assertEqual(expected['msg'], result['msg'])
        except Exception as e:
            # 定义异常，异常如何
            self.excel.write_data(row, column=8, value='未通过')
            # 写入未通过结果
            log.error('用例{}执行不通过'.format(case['title']))
            # format格式化，把case中的title写入{}
            log.exception(e)
            # 抛出异常
            raise e
            # 手动触发异常
        else:  # 否则就正常，正常又如何
            self.excel.write_data(row=row, column=8, value='通过')
            log.info('用例{}执行通过'.format(case['title']))

if __name__ == '__main__':
    unittest.main()
