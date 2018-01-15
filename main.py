#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: main.py
@time: 2018/1/15 15:49
"""

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)



