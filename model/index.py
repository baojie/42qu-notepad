#coding:utf-8

import _env
import time
from random import choice
from _db import connection, kv, McCache
from lib.txt_diff import diff_get
from model.history import mc_txt_brief, mc_url_id_list_by_user_id, KV_TXT_SAVE_TIME, history_count, txt_get, txt_set

KV_TXT_SAVE_TIME = "TxtSaveTime:"

URL_ENCODE = 'abcdefghijklmnopqrstuvwxyz0123456789'

        
 
def txt_by_url(url):
    url_id = url_new(url)
    return txt_get(url)

def url_random():
    while True:
        url = ''.join(choice(URL_ENCODE) for i in xrange(choice((7,8,9))))
        if not txt_by_url(url):
            break
    return url

mc_url_by_id = McCache("UrlById:%s")

@mc_url_by_id('{id}')
def url_by_id(id):
    cursor = connection.cursor()
    cursor.execute(
        'select url from url where id=%s',
        id
    )
    url = cursor.fetchone()
    return url[0] if url else None

mc_url_new = McCache("UrlNew:%s")

@mc_url_new("{url}")
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
    txt_old = kv.get(str(url_id))
    if txt_old == txt:
        return
    mc_txt_brief.delete(url_id)
    mc_url_id_list_by_user_id.delete(user_id)
    txt_set(url_id, txt)
    now = int(time.time())
    txt_touch(user_id, url_id)
    kv.set(KV_TXT_SAVE_TIME+str(url_id), now) 
    txt_log_save(user_id, url_id, txt, txt_old)

def txt_touch(user_id, url_id):
    if not user_id:return
    now = int(time.time())
    cursor = connection.cursor()
    cursor.execute('select id from user_note where url_id=%s and user_id=%s',(url_id, user_id))
    r = cursor.fetchone()
    if r:
        cursor.execute('update user_note set view_time=%s where id=%s',(now, r[0]))
    else:
        cursor.execute(
            'insert into user_note (user_id, url_id, view_time) values '
            '(%s,%s,%s) ON DUPLICATE KEY UPDATE view_time=%s',
            (user_id, url_id, now, now)
        )
        history_count.delete(user_id)

mc_txt_log_last_time = McCache("TxtLogLastTime:%s")

@mc_txt_log_last_time("{url_id}")
def txt_log_last_time(url_id):
    '''
    返回文本上次更新时间
    '''
    cursor = connection.cursor()
    cursor.execute(
        'select time from txt_log where url_id = %s order by time DESC',
        url_id
    )
    t = cursor.fetchone()
    return t[0] if t else 0

def txt_log_save(user_id, url_id, txt, txt_old):
    now = int(time.time())
    if txt_old and now - txt_log_last_time(url_id) > 600:
        cursor = connection.cursor()
        cursor.execute(
            'insert into txt_log (url_id, user_id, time) values (%s,%s,%s)',
            (url_id, user_id, int(time.time()))
        )
        id = cursor.lastrowid
        kv.set('TxtLog:%s' % id, txt_old)
        diff = diff_get(txt_old, txt)
        kv.set('TxtDiff:%s' % id, diff)
        mc_txt_log_last_time.set(id, now) 

if __name__ == "__main__":
    print url_new('sssafes')
