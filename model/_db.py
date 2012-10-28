#coding:utf-8


# 初始化数据连接
import _env
import MySQLdb
from DBUtils.PersistentDB  import PersistentDB as DB
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB
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
    mc = cmemcached.Client(memcached_addr, memcached_addr=MEMCACHED_ADDR)

from zorm_sae.mc_connection import init_mc
import zorm_sae.config as zorm_config

zorm_sae_config.mc = init_mc(
    disable_local_cached=DISABLE_LOCAL_CACHED
)
