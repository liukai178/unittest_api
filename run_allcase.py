# 自动执行所有测试，生成并发送报告至邮箱模块
import unittest
from common.HTMLTestRunnerCN美化加接口返回模板 import HTMLTestReportCN
from common.handlepath import *
import time
from common.HANDLE_EMAIL import send_email

# 格式化显示当前时间
now = time.strftime('%Y-%m-%d-%H-%M')
# 定义生成报告的名称
# filename = REPORTDIR + "\\" + str(now) + '_api_report.html'
filename = REPORTDIR + "\\" + 'api_report.html'
print(filename)

def auto_run():
    #自动生成测试报告
    #自动搜索测试用例
    discover = unittest.defaultTestLoader.discover(CASEDIR,'test_*.py')#根据需求选择筛选用例，此处是选择所有test开头的py文件
    #打开报告文件并写入
    f = open(filename,'wb')
    runner = HTMLTestReportCN(stream=f,
                              title="链铺接口自动化测试报告",
                              description='用例执行情况如下：',
                              tester='测试—刘凯')
    #运行HT中的run方法，参数为自动搜索出的用例
    runner.run(discover)
    #关闭文件
    f.close()

if __name__ == '__main__':
    auto_run()
    send_email(filename,"链铺接口自动化测试报告")