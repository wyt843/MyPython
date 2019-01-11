#! /usr/bin/env python
# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'wenyitao880901@126.com'
receivers = ['ibm_wyt@163.com', 'wenyitao880901@163.com'] # 接受邮件的地址

# 三个参数：第一个位文本内容，第二个位plain设置文本格式，第三个编码
message = MIMEText("邮件content", 'plain', 'utf-8')
# message 中 from 和 to 必须设置
message["from"] = "wenyitao880901@126.com"
message["to"] = "ibm_wyt@163.com"

subject = "Python SMTP mail testging"
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('smtp.126.com', 25)
    smtpObj.login('wenyitao880901@126.com', 'W8y4t3') # 登录

    print(message.as_string(True))
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except Exception as e:
    print(e.with_traceback())
