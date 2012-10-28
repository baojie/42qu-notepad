#coding:utf-8

import _env
import time
from _db import connection, kv, McNum, McCache, McLimitA
from lib.txt import cnenoverflow

mc_txt_brief = McCache("TxtBrief:%s")

def history_get(user_id, offset=0, limit=0):
    #[timestamp,content, url , count ]
    id_li = []
    time_li = []
    for id, view_time in url_id_list_by_user_id(user_id, limit, offset):
        id_li.append(id)
        time_li.append(view_time)
    digest_li = []
    count_li = []
    for id, i in zip(id_li, mc_txt_brief.get_list(id_list)):
        if i is None:
            txt = kv.get(str(id))
            i = cnenoverflow((txt, 333), len(txt))
            mc_txt_brief.set(id, i)
        digest_li.append(i[0])
        count_li.append(i[1])
    return zip(time_li, digest_li, id_li, count_li)

def history_count(user_id):
    cursor = connection.cursor()
    cursor.execute(
        'select count(url_id) from user_note where user_id = %s '
        'order by view_time DESC',
        (user_id)
    )
    return cursor.fetchone()[0]

mc_url_id_list_by_user_id = McLimitA("TxtBriefByUserId:%s", 64)
@mc_url_id_list_by_user_id("{user_id}")
def url_id_list_by_user_id(user_id, limit, offset):
    cursor = connection.cursor()
    cursor.execute(
        'select url_id, view_time from user_note where user_id = %s '
        'order by view_time DESC limit %s offset %s',
        (user_id, limit, offset)
    )
    return cursor.fetchall()




if __name__ == "__main__":
    pass
