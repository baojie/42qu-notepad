#coding:utf-8

import string
from _view import View
from random import choice
from model._db import connection
from time import time


def account_new(username, email):
    u, e = map(string,strip, (username, email))
    if not user_id_by_email(e):
        cursor = connection.cursor()
        if txt:
            cursor.execute(
                'insert into notepad (url,txt,`time`) values '
                '(%s,%s,%s) ON DUPLICATE KEY UPDATE txt=%s,`time`=%s',
                (url, txt, now, txt, now)
            )
    
    pass

def user_id_by_email(email):
    cursor = connection.cursor()
    cursor.execute('select id from account where email=%s',email)
    user_id = cursor.fetchone()
    if user_id:
        user_id = user_id[0]
    else:
        user_id = 0
    return user_id


    def post(self, url):
        if url:
            url = url.lower()
            txt = self.get_argument('txt', '').rstrip()
            now = time()
            cursor = connection.cursor()
            if txt:
                cursor.execute(
                    'insert into notepad (url,txt,`time`) values '
                    '(%s,%s,%s) ON DUPLICATE KEY UPDATE txt=%s,`time`=%s',
                    (url, txt, now, txt, now)
                )
            else:
                cursor.execute('delete from notepad where url=%s', url)
        self.finish({'time':now})
