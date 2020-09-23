from public.pages.BaseTestCase import BaseTestCaase
import unittest
from public.utils.Login_Data import Login_Data as login
from selenium import webdriver
import time
#导入页面所有的元素值作为P
from public.pages.Page_Element import Page_Element as P
class Test_Self_Center(BaseTestCaase):
    @classmethod
    def setUpClass(cls):
        BaseTestCaase.sleep(3)


    @classmethod
    def tearDownClass(cls):
        BaseTestCaase.sleep(3)
        BaseTestCaase.goto_homeself()

    # def setUp(self):
    #     print("方法开始")
    #
    # def tearDown(self):
    #     print("方法结束")

    def test001_self_center(self):
        # try:
        # 定位个人中心，然后点击
        m = BaseTestCaase.find_element(P.myself)
        BaseTestCaase.click(m)
        # 定位个人中心页面中的个人中心字样
        text = BaseTestCaase.get_text(P.selfinfor)
        print(text)
        self.assertEqual(text, u"个人信息")
        # assert text == u"个人中心"
        # except Exception as e:
        #     print(e.message)
