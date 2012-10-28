#coding:utf-8

import _env
import time
from random import choice
from _db import connection, kv
from lib.txt_diff import diff_get
    

URL_ENCODE = 'abcdefghijklmnopqrstuvwxyz0123456789'

def txt_by_url(url):
    url_id = url_new(url)
    return kv.get(str(url_id)) or ''

def gen_url():
    while True:
        url = ''.join(choice(URL_ENCODE) for i in choice((7,8,9)))
        if not txt_by_url(url):
            break
    return url

def url_by_id(id):
    cursor = connection.cursor()
    cursor.execute(
        'select url from url where id=%s',
        id
    )
    url = cursor.fetchone()
    return url[0] if url else ''

def url_new(url):
    url = str(url.lower())
    cursor = connection.cursor()
    cursor.execute('select id from url where url=%s', url)
    id = cursor.fetchone()
    if id:
        return id[0]
    else:
        cursor.execute('insert into url (url) values(%s)', url)
        return cursor.lastrowid

def txt_save(user_id, url, txt):
    url_id = url_new(url)
    txt_ori = kv.get(str(url_id))
    if txt_ori == txt:
        return
    kv.set(str(url_id), txt or '')
    if user_id:
        now = int(time.time())
        cursor = connection.cursor()
        cursor.execute(
            'insert into user_note (user_id, url_id, view_time) values '
            '(%s,%s,%s) ON DUPLICATE KEY UPDATE view_time=%s',
            (user_id, url_id, now, now)
        )
    txt_log_save(user_id, url_id, txt, txt_ori)

def last_update(url_id):
    '''
    返回文本上次更新时间
    '''
    print 'LAST UPDATE', url_id
    cursor = connection.cursor()
    cursor.execute(
        'select time from txt_log where url_id = %s order by time DESC',
        url_id
    )
    t = cursor.fetchone()
    return t[0] if t else 0

def txt_log_save(user_id, url_id, txt, txt_ori):
    now = int(time.time())
    if txt_ori and now - last_update(url_id) > 2:
        print 'save log-----------'
        cursor = connection.cursor()
        cursor.execute(
            'insert into txt_log (url_id, user_id, time) values (%s,%s,%s)',
            (url_id, user_id, int(time.time()))
        )
        id = cursor.lastrowid
        kv.set('o_%s' % id, txt_ori)
        diff = diff_get(txt_ori, txt)
        kv.set('d_%s' % id, diff)    

if __name__ == "__main__":
    print url_new('sssafes')
