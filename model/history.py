#coding:utf-8

import _env
import time
from _db import connection, kv

def history_get(user_id, offset=0, limit=0):
    #[timestamp,content, url , count ]
    cursor = connection.cursor()
    cursor.execute(
        'select url_id, view_time from user_note where user_id = %s '
        'order by view_time DESC limit %s offset %s',
        (user_id, limit, offset)
    )
    _history = cursor.fetchall()
    id_li = [str(i[0]) for i in _history]
    time_li = [i[1] for i in _history]
    txt_dict = kv.get_multi(id_li)
    txt_li = [txt_dict[i] for i in id_li]
    count_li = [len(i) for i in txt_li]
    return zip(time_li, txt_li, id_li, count_li)
    
def history_count(user_id):
    cursor = connection.cursor()
    cursor.execute(
        'select count(url_id) from user_note where user_id = %s '
        'order by view_time DESC',
        (user_id)
    )
    return cursor.fetchone()[0]


if __name__ == "__main__":
    pass
