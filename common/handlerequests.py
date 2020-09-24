# 处理接口请求
import requests
class SendRequests(object):
    def __init__(self):
#为了让登录和登录后的接口保持在同一个会话当中
        self.session = requests.session()

    def send(self,method, url, params=None, data=None, headers=None, json=None):
        method = method.lower()
#把请求方式转换为小写
        if method == "get":
            response = self.session.get(url, params, headers)
        elif method == "post":
            response = self.session.post(url, data, headers)
            return response





