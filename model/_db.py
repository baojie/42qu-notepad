#coding:utf-8


# 初始化数据连接
import MySQLdb
from DBUtils.PersistentDB  import PersistentDB as DB

def _connection(*args, **kwds):
    kwds['maxusage'] = False
    persist = DB (MySQLdb, *args, **kwds)
    conn = persist.connection()
    return conn

connection = _connection(host='127.0.0.1', user='root', passwd='42qu', db='work_notepad')
