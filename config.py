#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from os.path import dirname, abspath, exists, join
from mako.lookup import TemplateLookup


DEBUG = True
PREFIX = dirname(abspath(__file__))

_lookup = TemplateLookup(
    directories=join(PREFIX, 'html'),
    module_directory='/tmp/mako',
    disable_unicode=True,
    encoding_errors='ignore',
    default_filters=['str', 'h'],
    filesystem_checks=DEBUG,
    input_encoding='utf-8',
    output_encoding=''
)


def render(html, **kwds):
    return _lookup.get_template(html).render(**kwds)


import MySQLdb
from DBUtils.PersistentDB  import PersistentDB as DB

def _connection(*args, **kwds):
    kwds['maxusage'] = False
    persist = DB (MySQLdb, *args, **kwds)
    conn = persist.connection()
    return conn

connection = _connection(host='127.0.0.1', user='root', passwd='42qu', db='work_notepad')
