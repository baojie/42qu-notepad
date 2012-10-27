#coding:utf-8

import _env
import time
from _db import connection, kv

def history_get(user_id, offset=0, limit=0):
    cursor = connection.cursor()
    cursor.execute(
        'select url_id, view_time from user_note where user_id = %s '
        'order by view_time DESC limit %s offset %S',
        (user_id, limit, offset)
    )
    _history = cursor.fetchall()
    cursor.execute(
        'select url from url where '
    )
    _li = [i for i in _history]
    #[timestamp,content, url , count ]
    


if __name__ == "__main__":
    pass
