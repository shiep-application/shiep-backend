import yaml
from email.mime.text import MIMEText
from email.header import Header
import socket
import requests
import json
import time
import smtplib
import copy
import os


def read_config():
    print(os.getcwd())
    f = open(os.getcwd() + "/mail_sending_config.yml", 'r', encoding='utf-8')
    return yaml.load(f.read())


def generate_html(grades):
    html = """<html lang="zh-cn">
                <head>
                    <title>成绩明细</title>
                    <style>
                        tr, td, th, table {
                            border: 1px solid black;
                        }
                    </style>
                </head>
                <body>
                <table style='text-align: center'>
                    <tr>
                        <td>课程名称</td>
                        <td>学分数</td>
                        <td>成绩</td>
                        <td>授课教师</td>
                    </tr> 
    """
    for item in grades:
        row = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td>".format(item["kcmc"], item["kcxf"], item["cj"], item["rkjs"])
        html = html + row
    html = html + """
                </table>
            </body>
        </html>"""
    print(html)
    text_html = MIMEText(html, 'html', 'utf-8')
    text_html["Content-Disposition"] = 'attachment; filename="scores.html"'
    return text_html


def sendmail(subject, message, config, user_mail):
    mail_host = config["mail_host"]
    mail_user = config["mail_user"]
    print(mail_user)
    mail_token = config["mail_token"]
    print(mail_token)
    sender = config["mail_user"]
    receivers = user_mail
    message['From'] = Header('S-Server<score@shiep_xyy.edu.cn>', 'utf-8')
    message['To'] = Header(receivers + '<' + receivers + '>', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        SMTPObj = smtplib.SMTP_SSL(mail_host, 465)
        SMTPObj.ehlo()
        SMTPObj.login(mail_user, mail_token)
        SMTPObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPAuthenticationError:
        print("邮箱账号或密码错误")
    except socket.gaierror:
        print("网络连接错误，请检查SMTP服务器配置")


