#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')





def pre_config(o):
    o.HOST = "42qu.cc"
    o.MYSQL_HOST = '127.0.0.1'
    o.MYSQL_PORT = 3306
    o.MYSQL_USER = 'work'
    o.MYSQL_PASSWD = '42qu'
    o.MYSQL_DB = 'work_notepad'
    o.DEBUG = True
    from render import render
    o.render = render

def post_config(o):
    o.HOST_CSS_JS = 's.%s'%o.HOST

#    o.URL_CSS_JS = '//%s'%o.HOST_CSS_JS

