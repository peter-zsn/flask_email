#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: main.py
@time: 2018/1/15 15:49
"""
import time
from flask import Flask
from flask.ext.mail import Mail, Message
import os

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.exmail.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='zhangshuainan@tbkt.cn',
    MAIL_PASSWORD='ZSN1993zsn',
    MAIL_DEBUG=True,
)

mail = Mail(app)

@app.route('/')
def index():
    msg = Message("大壮是逗比", sender='zhangshuainan@tbkt.cn', recipients=['lvyang@tbkt.cn',
                                                                        'zhangshuainan@tbkt.cn'])
    msg.body = "瑶瑶， 你同事长的挺帅的"
    mail.send(msg)
    return "sent"

@app.route('/html/')
def index_html():
    content_title = '''<table width="100%%" border="1" cellspacing="0"  >
      <tr>
        <td align="center">名字</td>
        <td align="center">性别</td>
        <td align="center">年龄</td>
      </tr>
    '''

    data_format = '''  <tr>
    <td align="center">%s</td>
    <td align="center">%s</td>
    <td align="center"><font color='red'>%s</font></td>
    </tr>'''

    data_list = [('小李', '男', '25'), ('小李1', '男', '25'), ('小李2', '男', '25')]
    content = content_title
    for obj in data_list:
        content += data_format % obj

    content += "</table><br/><br/>"

    subject = '孤独者的自白'
    msg = Message(subject, sender='zhangshuainan@tbkt.cn', recipients=['zhangshuainan@tbkt.cn'])
    msg.html = content
    mail.send(msg)

    return "sent_html"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)



