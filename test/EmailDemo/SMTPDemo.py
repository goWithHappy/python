#构造一个简答的纯文本邮件,在此种情况下会被网易云认为是垃圾邮件
import smtplib
from email.mime.text import MIMEText

msg=MIMEText('hello,send by Python..','Plain','utf-8')
# #第一个参数是邮件正文，第二个参数是MIME的subtype，传入plain表示纯文本，最终MIME是‘text/plain’，最后要用utf-8
# #通过SMTP把邮件发出去：
# from_addr=input('From:')
# password=input('Password:')
# #输入收件人地址：
# to_addr=input('TO:')
# #输入SMTP服务器地址
# smtp_server=input('SMTP server:')
# server=smtplib.SMTP(smtplib,25) #SMTP默认的端口是25
# server.set_debuglevel(1)    #set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()
# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()