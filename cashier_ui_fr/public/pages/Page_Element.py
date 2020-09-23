# coding=utf-8
'''
此模块是为了存放所有页面的元素
Java当中的设计模式
PO设计模式 ==》 全称叫做page_object(页面对象模型）
把所有页面上的元素都作为对象的或者类的属性
把元素和流程分开
降低代码的耦合度，容易维护
'''
class Page_Element:
    #登录模块
    #登录按钮的定位方式和元素值
    loginvalue = ("css","body > section.header-container > header > div.header-nav-wrap > nav > ul > li:nth-child(7) > a:nth-child(1)")
    uservalue = ("css", "#loginForm > input")
    codevalue = ("css", "#loginForm > div.verification > input")
    pwdvalue = ("css", "#loginForm > div.password-login > div.password-wrap > input")
    agreevalue = ("css", "#loginForm > div.remember-agree > div > label")
    submitvalue = ("css", "#loginForm > button")
    homevalue = ("css", "body > section.header-container > header > div.header-nav-wrap > nav > ul > li:nth-child(1) > a")
    homevalueself = ("css", "body > section.nav-wrapper > nav > ul > li:nth-child(2) > a")
    loginoutvalue = ("link",u"退出登录")

    #个人中心模块
    myself = ("css","body > section.header-container > header > div.header-nav-wrap > nav > ul > li:nth-child(7) > a:nth-child(1)")
    selfinfor = ("link",u"个人信息")