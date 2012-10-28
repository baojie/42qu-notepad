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

    mc_txt_brief_by_user_id = McLimitM("TxtBriefByUserId:%s", 512)
    
    @mc_txt_brief_by_user_id("{user_id}")
    def txt_brief_by_user_id(user_id, limit, offset):
        return ('32223232 ...',32)

    print txt_brief_by_user_id(1,3,0)

