# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText

email_host = 'smtp.qq.com'     # smtp server
email_user = '1398869507@qq.com'  # sender mail address
email_pwd = 'bajebthewpuyhagb'  # password
maillist ='jeason3532016@gmail.com' # mail of receiver

me = email_user
msg = MIMEText('test')    # 邮件内容
msg['Subject'] = 'python测试'    # 邮件主题
msg['From'] = me    # 发送者账号
msg['To'] = maillist    # 接收者账号列表
smtp = smtplib.SMTP_SSL(email_host, 465)
# smtp.starttls()  # open SSL
# smtp.set_debuglevel(1)
smtp.login(email_user, email_pwd)   # login
smtp.sendmail(me, maillist, msg.as_string())
# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
smtp.quit() # 发送完毕后退出smtp
print ('email send success.')
