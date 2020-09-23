#coding = utf-8
import unittest
# from HTMLTestRunner import HTMLTestRunner
# from public.HTMLTestRunnerCN import HTMLTestReportCN
from public.HTMLTestRunnerCN美化加接口返回模板 import HTMLTestReportCN
#导入全局变量(公共文件的路径)
from config import globalconfig
from public.HANDLE_EMAIL import send_email
import time
now = time.strftime("%Y-%m-%d-%H-%M-%S")
# print(now)
report_path = globalconfig.report_path
filename = report_path + '\\' + str(now) + 'ui_report.html'
# print(path)
def aoto_run():
    #创建一个套件，容器用来装测试用例
    suite = unittest.TestSuite()
    # 加载器
    loader = unittest.TestLoader()
    # 用加载器往容器中装测试用例(参数为文件路径、用例类、用例方法)
    suite.addTest(loader.loadTestsFromName("public.pages.login.TestLogin.testLogin"))
    suite.addTest(loader.loadTestsFromName("TestCase.Test_Self_Center1.Test_Self_Center.test001_self_center"))
    print(suite)

    #生成测试报告
    #生成报告的文件路径
    f = open(filename,"wb")
    # 创建生成报告的执行器，编辑报告的标题等信息
    runner = HTMLTestReportCN(stream=f,title=u"链铺项目UI自动化测试报告",
                            description=u"用例执行情况如下",tester=u"刘凯")
    #运行执行器的run函数（参数为装满用例的套件）
    runner.run(suite)

def Send_mail():
    send_email(filename,u"链铺项目UI自动化测试报告")



if __name__ == '__main__':
    aoto_run()
    Send_mail()
















