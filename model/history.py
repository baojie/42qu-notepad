#coding:utf-8

import _env
import time
from _db import connection, kv, McNum, McCache, McLimitM
from lib.txt import cnenoverflow
from time import time
from index import KV_TXT_SAVE_TIME
mc_txt_brief = McCache("TxtBrief:%s")

def history_get(user_id, offset=0, limit=0):
    #[timestamp,content, url , count ]
    id_li = []
    time_li = []
    for id, view_time in url_id_time_list_by_user_id(user_id, limit, offset):
        id_li.append(id)
        time_li.append(view_time)
    digest_li = []
    count_li = []
    for id, i in zip(id_li, mc_txt_brief.get_list(id_li)):
        if i is None:
            txt = kv.get(str(id))
            i = (cnenoverflow(txt, 96)[0], len(txt.decode('utf-8',"ignore")))
            mc_txt_brief.set(id, i)
        digest_li.append(i[0])
        count_li.append(i[1])
    return zip(time_li, digest_li, id_li, count_li)

def history_count(user_id):
    cursor = connection.cursor()
    cursor.execute(
        'select count(url_id) from user_note where user_id = %s ', user_id
    )
    return cursor.fetchone()[0]

mc_url_id_list_by_user_id = McLimitA("UrlListByUserId<%s", 256)
@mc_url_id_list_by_user_id("{user_id}")
def url_id_list_by_user_id(user_id, limit, offset):
    cursor = connection.cursor()
    cursor.execute(
        'select url_id from user_note where user_id = %s '
        'order by view_time DESC limit %s offset %s',
        (user_id, limit, offset)
    )
    return [i[0] for i in cursor]


def url_id_time_list_by_user_id(user_id, limit, offset):
    id_list = url_id_list_by_user_id(user_id, limit, offset)
    time_dict =  kv.get_mulit(id_list,key_prefix=KV_TXT_SAVE_TIME)
    result = []
    for i in map(str,id_list):
        _time = time_dict[i]
        if not _time:
            _time = time()
            kv.set(KV_TXT_SAVE_TIME+i,_time) 
        result.append(i,_time)

    return result 

if __name__ == "__main__":
    pass
    
