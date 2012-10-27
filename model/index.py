#coding:utf-8

import _env
import time
from random import choice
from _db import connection
try:
    from sae.kvdb import KVClient as kv
except:
    from kvstore import kv
    
    

URL_ENCODE = 'abcdefghijklmnopqrstuvwxyz0123456789'

def _txt_by_url(url):
    url = url.lower()
    cursor = connection.cursor()
    cursor.execute('select txt from notepad where url=%s', url)
    txt = cursor.fetchone()
    if txt:
        txt = txt[0]
    else:
        txt = ''
    return txt

def txt_by_url(url):
    url = str(url.lower())
    db = kv()
    return db.get(url) or ''

def gen_url():
    while True:
        url = ''.join(choice(URL_ENCODE) for i in xrange(9))
        if not txt_by_url(url):
            break
    return url


def _save_txt(url, txt):
    now = int(time.time())
    cursor = connection.cursor()
    if txt:
        cursor.execute(
            'insert into notepad (url,txt,`time`) values '
            '(%s,%s,%s) ON DUPLICATE KEY UPDATE txt=%s,`time`=%s',
            (url, txt, now, txt, now)
        )
    else:
        cursor.execute('delete from notepad where url=%s', url)

def save_txt(url, txt):
    url = str(url.lower())
    db = kv()
    if txt:
        db.set(url, txt)
    else:
        db.set(url, '')
