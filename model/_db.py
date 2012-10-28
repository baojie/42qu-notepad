#coding:utf-8


# 初始化数据连接
import _env
import MySQLdb
from DBUtils.PersistentDB  import PersistentDB as DB
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB, DISABLE_LOCAL_CACHED
def _connection(*args, **kwds):
    kwds['maxusage'] = False
    persist = DB (MySQLdb, *args, **kwds)
    conn = persist.connection()
    return conn

connection = _connection(
    host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB, charset='utf8'
)

try:
    from sae.kvdb import KVClient
    kv = KVClient()
    import pylibmc
    mc = pylibmc.Client()
except:
    from kvstore import kv
    import cmemcached
    from config import MEMCACHED_ADDR
    kw = {}
    kw['comp_threshold'] = 4096
    mc = cmemcached.Client(MEMCACHED_ADDR)

from zorm_sae.mc_connection import init_mc
import zorm_sae.config 

zorm_sae.config.mc = init_mc(
    mc,
    disable_local_cached=DISABLE_LOCAL_CACHED
)

from zorm_sae.mc import McCacheM, McCache, McNum, McCache, McLimitA, McCacheA, McLimitM

if __name__ == "__main__":
    mc_url_id_list_by_user_id = McLimitA("TxtBriefByUserId:%s", 64)

    #mc_user_last_view_id = McCache("UserLastView:%s")
    
 
    @url_id_list_by_user_id("{user_id}")
    def url_id_list_by_user_id(user_id, limit, offset):
        return (1,2,3) 
  
    mc_txt_brief = McCache("TxtBrief:%s")
 
    def txt_list_by_user_id(user_id):
        id_list = url_id_list_by_user_id(user_id, limit, offset)
        result = []
        for id, i in zip(id_list, mc_txt_brief.get_list(id_list)):
            if i is None:
                txt = kv.get("Txt:%s"%id)
                i = (cnenoverflow(txt, 333),字数)
                mc_txt_brief.set(id, i)
            result.append(i) 
 
     

    
