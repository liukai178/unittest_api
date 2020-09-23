#coding = utf-8
'''
基类
'''

import unittest
from selenium import webdriver
import time
from public.pages.Page_Element import Page_Element as P
class BaseTestCaase(unittest.TestCase):
    '''
    所有页面的公共方法都封装在这个基类中
    需求：打开一个浏览器--输入网址--定位百度输入框元素--输入内容--点击按钮
    '''
    #类方法
    @classmethod
    def set_driver(cls,driver):
        '''
        设置driver对象
        用来保证每个用例的执行都是调用的同一个driver对象
        Java当中的设计模式--单例模式
        实现原理：每个用例执行前调用set_driver,跑完后再传给get_driver这个函数，
        下个用例接着调用这个driver
        '''
        # 把driver传给类属性（cls.driver）
        cls.driver = driver

    @classmethod
    def get_driver(cls):
        return cls.driver
    # driver = webdriver.Chrome()

    @classmethod
    #element是个元组，里面有定位方式和要定位的元素
    def find_element(cls,element):
        #元组第一个索引为方式，第二个索引为该方式对应的元素
        type = element[0]
        value = element[1]
        try:
            if type =="id" or type =="Id" or type =="ID":
                elem = cls.driver.find_element_by_id(value)
            elif type =="name" or type =="Name" or type =="NAME":
                elem = cls.driver.find_element_by_name(value)
            elif type =="class" or type =="Class" or type == "CLASS":
                elem = cls.driver.find_element_by_class_name(value)
            elif type == "xpath" or type == "Xpath" or type == "XPATH":
                elem = cls.driver.find_element_by_xpath(value)
            elif type == "css" or type =="Css" or type == "CSS":
                elem = cls.driver.find_element_by_css_selector(value)
            elif type == "link" or type == "Link" or type == "LINK":
                elem = cls.driver.find_element_by_link_text(value)
            else:
                raise NameError("please input correct parameter!!")
        except Exception:
            raise NameError("this element not found")
        return elem
    @classmethod
    #element就是定位到的元素，然后输入text
    # ''' #输入用户名
    #     user = BaseTestCaase.find_element(P.uservalue)
    #     #此处的usernamenum是从excel读取的
    #     BaseTestCaase.send_keys(user,usernamenum)
    # '''
    def send_keys(cls,element,text):
        element.send_keys(text)

    @classmethod
    def click(cls,element):
        element.click()

    @classmethod
    def sleep(cls,sec):
        return time.sleep(sec)

    @classmethod
    def wait(cls,sec):
        return cls.driver.implicitly_wait(sec)

    @classmethod
    def close(cls):
        return cls.driver.close()

    @classmethod
    def get_title(cls):
        title = cls.driver.title
        return title

    @classmethod
    #locator是一个元组，等同于element
    def get_text(cls,locator):
        text = BaseTestCaase.find_element(locator).text
        return text

    @classmethod
    #每次跑完用例回到首页
    def goto_home(cls):
        home = BaseTestCaase.find_element(P.homevalue)
        BaseTestCaase.click(home)

    @classmethod
    # 从个人中心回到首页
    def goto_homeself(cls):
        homeself = BaseTestCaase.find_element(P.homevalueself)
        BaseTestCaase.click(homeself)







