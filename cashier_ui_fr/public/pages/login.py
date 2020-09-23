from public.pages.BaseTestCase import BaseTestCaase
import unittest
from public.utils.Login_Data import Login_Data as login
from selenium import webdriver
import time
#导入页面所有的元素值作为P
from public.pages.Page_Element import Page_Element as P
url = login.get_url()
usernamenum = login.get_username()
codenum = login.get_code()
pwdnum = login.get_pwd()
class TestLogin(BaseTestCaase):
    # url = login.get_url()
    @classmethod
    def setUpClass(cls):
        #设置driver（打开浏览器）
        driver = webdriver.Chrome()
        #设置driver为全局
        BaseTestCaase.set_driver(driver)

    @classmethod
    def tearDownClass(cls):
        #每次跑完用例之后的清理工作，此处是回到首页
        BaseTestCaase.sleep(3)
        BaseTestCaase.goto_home()

    def testLogin(self):
        '''
        第一个用例为登录，需要打开浏览器，输入网址并登录;
        后续如果不用重新打开浏览器，则不用调用get_driver
        :return:
        '''
        #调用set好的driver，后续其他用例如果需要重新打开此浏览器也可如此调用，浏览器没关则不用
        driver = BaseTestCaase.get_driver()
        BaseTestCaase.wait(3)
        # driver.get(url)
        # BaseTestCaase.get_driver().get(url)
        driver.maximize_window()
        driver.get(url)#打开测试网址
        BaseTestCaase.wait(20)
        #点击登录按钮
        #登录按钮的定位方式和值
        # loginvalue = ("css","body > section.header-container > header > div.header-nav-wrap > nav > ul > li:nth-child(7) > a:nth-child(1)")
        #定位登录按钮（参数为上方面的login或者P中的对应元素值,下面方式一样）
        loginbutton = BaseTestCaase.find_element(P.loginvalue)
        #点击登录按钮(参数为上面的定位到的登录按钮loginbutton)
        BaseTestCaase.click(loginbutton)
        #输入用户名
        user = BaseTestCaase.find_element(P.uservalue)
        #此处的usernamenum是从excel读取的
        BaseTestCaase.send_keys(user,usernamenum)
        #输入验证码
        # codevalue = ("css","#loginForm > div.verification > input")
        code = BaseTestCaase.find_element(P.codevalue)
        BaseTestCaase.send_keys(code,codenum)
        #输入密码
        # pwdvalue = ("css","#loginForm > div.password-login > div.password-wrap > input")
        pwd = BaseTestCaase.find_element(P.pwdvalue)
        BaseTestCaase.send_keys(pwd,pwdnum)
        # 点击同意协议
        # agreevalue = ("css","#loginForm > div.remember-agree > div > label")
        agree = BaseTestCaase.find_element(P.agreevalue)
        BaseTestCaase.click(agree)
        # 点击确定提交
        # submitvalue = ("css","#loginForm > button")
        submit = BaseTestCaase.find_element(P.submitvalue)
        BaseTestCaase.click(submit)
        BaseTestCaase.wait(2)
        #断言
        text = BaseTestCaase.get_text(P.loginoutvalue)
        print(text)
        assert text == u"退出登录"



if __name__ == '__main__':
    unittest.main()