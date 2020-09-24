#测试用例
import unittest
from common.handlerequests import SendRequests
from common.handlelog import log
from common.readexcel import ReadExcel
from common.ddt import data,ddt
from common.handleconfig import conf
from common.handlepath import *
import os
case_file = os.path.join(DATADIR,"apicase.xlsx")
@ddt()
class Test_Login(unittest.TestCase):
    excel = ReadExcel(case_file,"login")
    cases = excel.read_data()
    request = SendRequests()

    @data(*cases)   #可变长参数，接收多条用例，因为cases中有多条用例数据，多条字典
    def test001_login(self,case):
#第一步：准备接口请求
        url = conf.get("env","url") + case["url"]
        print(url)
        method = case['method']
        print(method)
        data = eval(case['data'])
        #eval这个内置函数的作用：执行一个字符串表达式，并且返回执行后的结果
        headers = eval(conf.get('env','headers'))
        #从配置文件文件config.ini中取header等常用请求头信息或者接口参数
        expected = eval(case['expected'])
        #从excel取expected预期结果内容
        row = case['case_id'] + 1
        #每跑一行，case_id + 1

#第二步，发送接口请求
        response = self.request.send(method=method,url=url,headers=headers,data=data)
        print(response.json())
        result = response.json()

#第三步：接口的断言
        try:        #期待值和实际结果值对比断言
            self.assertEqual(expected['code'], result['code'])
            self.assertEqual(expected['msg'], result['msg'])
        except Exception as e:
            #定义异常，异常如何
            self.excel.write_data(row,column=8,value='未通过')
            #写入未通过结果
            log.error('用例{}执行不通过'.format(case['title']))
            #format格式化，把case中的title写入{}中
            log.exception(e)
            #抛出异常
            raise e
            #手动触发异常
        else:       #否则就正常，正常又如何
            self.excel.write_data(row=row,column=8,value='通过')
            log.info('用例{}执行通过'.format(case['title']))

if __name__ == '__main__':
    unittest.main()