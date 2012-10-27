#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 初始化 mako 模版 的 查找
from os.path import dirname, abspath, exists, join
from mako.lookup import TemplateLookup


DEBUG = True
PREFIX = dirname(dirname(abspath(__file__)))

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




def pre_config(o):
    o.HOST = "42qu.cc"
    o.MYSQL_HOST = '127.0.0.1'
    o.MYSQL_PORT = '3306'
    o.MYSQL_USER = 'work'
    o.MYSQL_PASSWD = '42qu'
    o.DEBUG = True
    from render import render
    o.render = render

def post_config(o):
    o.HOST_CSS_JS = 's.%s'%o.HOST

#    o.URL_CSS_JS = '//%s'%o.HOST_CSS_JS

