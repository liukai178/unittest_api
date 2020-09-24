#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2020/5/20 17:24
Wechat:15367499889
Company:上海多测师信息有限公司
===========================
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from common.handleconfig import conf


def send_email(filename, title):
    """
    发送邮件的功能函数
    :param filename: 文件的路径
    :param title:   邮件的主题
    :return:
    """
    # 第一步：连接邮箱的smtp服务器，并登录
    smtp = smtplib.SMTP_SSL(host=conf.get("email", "host"), port=conf.getint("email", "port"))
    smtp.login(user=conf.get("email", "user"), password=conf.get("email", "pwd"))

    # 第二步：构建一封邮件
    # 创建一封多组件的邮件
    msg = MIMEMultipart()

    with open(filename, "rb") as f:
        content = f.read()
    # 创建邮件文本内容
    text_msg = MIMEText(content, _subtype="html", _charset="utf8")
    # 添加到多组件的邮件中
    msg.attach(text_msg)
    # 创建邮件的附件
    report_file = MIMEApplication(content)
    report_file.add_header('content-disposition', 'attachment', filename=os.path.split(filename)[-1])
    # 将附件添加到多组件的邮件中
    msg.attach(report_file)

    # 主题
    msg["Subject"] = title
    # 发件人
    msg["From"] = conf.get("email", "from_addr")
    # 收件人
    msg["To"] = conf.get("email", "to_addr")

    # 第三步：发送邮箱
    smtp.send_message(msg, from_addr=conf.get("email", "from_addr"), to_addrs=conf.get("email", "to_addr"))





