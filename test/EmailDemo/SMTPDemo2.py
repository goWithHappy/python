# #增强版邮件发送，包含邮件的主题，收件人姓名等
# import smtplib
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
#
#
# def _fromat_addr(s):
#     name,addr=parseaddr(s)
#     return formataddr((Header(name,'utf-8').encode,addr))
# from_addr=input('From:')
# password=input('password')
# to_addr=input('TO:')
# smtp_server=input('SMP server:')
#
# msg=MIMEText('hello,send by Python..','Plain','utf-8')
# msg['F']=_fromat_addr('Python爱好者<%s>'%from_addr)
# msg['T']=_fromat_addr('管理员<%s>'%to_addr)
# msg['Subject']=Header('来自SMTP的问候...','utf-8')
#
# server=smtplib.SMTP(smtp_server,25)
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()