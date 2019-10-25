# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from global_ import global_cls
from utils import log

mylogger = log.Logger(logger='send_email').getlog()
# 第三方 SMTP 服务
mail_host = global_cls.email_server  # 设置服务器
mail_user = global_cls.email_user  # 用户名
mail_pass = global_cls.email_pass  # 口令

sender = mail_user  # 发送邮件
receivers = global_cls.email_receivers  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message = MIMEMultipart()  # 创建一个带附件的实例
message['From'] = sender  # 发件人地址
message['To'] = 'my fans'  # 收件人地址
subject = 'Automation Test Result'  # 发送邮件主题
testCase_path = global_cls.testCase_path


def send_mail(report_path, log_path):
    message['Subject'] = Header(subject, 'utf-8')
    # 正文
    mes = 'Dear All: <br/>' \
          '    这是自动测试的报告，请下载附件。 <br/>' \
          '    Thanks <br/>' \
          'FengHuJie<br/>'
    html_start = '<font face="Courier New, Courier, monospace"><pre>'
    html_end = '</pre></font>'
    message.attach(MIMEText(html_start + mes + html_end, 'html', 'utf-8'))
    # 附件报告
    att1 = MIMEText(open(report_path, 'rb').read(), 'html', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="result.html"'
    message.attach(att1)
    # 附件log日志
    att2 = MIMEText(open(log_path, 'rb').read(), 'html', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="logger.log"'
    message.attach(att2)
    # 附件测试用例
    att3 = MIMEText(open(testCase_path, 'rb').read(), 'html', 'utf-8')
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename="testCase.xls"'
    message.attach(att3)
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        mylogger.info('邮件发送成功！')
    except smtplib.SMTPException as e:
        mylogger.error('Error: cannot send my email')
        mylogger.error(e)


def send_log(report_path):
    return print(report_path)
