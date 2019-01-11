#! /usr/bin/env python
# coding:utf-8

from email.mime.text import MIMEText    # 构造附件使用
from email.mime.multipart import MIMEBase,MIMEMultipart # 构造基础邮件使用
import smtplib
mail_mul = MIMEMultipart('alternative')
mail_mul["From"] = 'wenyitao880901@126.com'
mail_mul["To"] = 'ibm_wyt@163.com'
mail_mul["Subject"] = '邮件标题'

# text 格式邮件
mail_text = MIMEText("text 格式邮件", "plain", "utf-8")
mail_mul.attach(mail_text)

# html 格式邮件
with open("mail.html", 'rb') as f:
    mail_html = MIMEText(f.read(), "html", "utf-8") # 构造邮件正文
    mail_mul.attach(mail_html)  # 把构造好的邮件正文加入邮件中



try:
    sender = 'wenyitao880901@126.com'
    receivers = ['ibm_wyt@163.com', 'wenyitao880901@163.com']  # 接受邮件的地址

    smtpObj = smtplib.SMTP('smtp.126.com', 25)
    smtpObj.login('wenyitao880901@126.com', 'W8y4t3') # 登录

    print(mail_mul.as_string(True))
    smtpObj.sendmail(sender, receivers, mail_mul.as_string())
    print("邮件发送成功")
except Exception as e:
    print(e.with_traceback())