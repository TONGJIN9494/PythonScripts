# -*- coding:UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from os.path import getsize
from sys import exit
from re import compile, IGNORECASE
import sys, time
import os

# 定义主机 帐号 密码 收件人 邮件主题

# 定义主机 帐号 密码 收件人 邮件主题


# 发送邮件函数
def send_mail():
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "xx@qq.com"  # 用户名
    mail_pass = "xx"  # 口令
    sender = 'xx@qq.com'
    receivers = ['xx@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def isRunning(process_name):
    try:
        process = len(os.popen('ps aux | grep "' + process_name + '" | grep -v grep').readlines())
        if process >= 1:
            return True
        else:
            return False
    except:
        print("Check process ERROR!!!")
        return False


# 调用发送邮件函数发送邮件
if __name__ == '__main__':
    process_name = "tomcat"
    isrunning = isRunning(process_name)
    print(isrunning)
    if isrunning == False:
        send_mail()
