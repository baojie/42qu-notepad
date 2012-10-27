#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')





def pre_config(o):
    o.HOST = "42qu.cc"
    o.HOST_CSS_JS = o.HOST
    o.HOST_DEV_PREFIX = "" 
    o.JS_CONST = o.HOST
    try:
        import sae.const
    except ImportError:
        o.DEBUG = True 
        o.MYSQL_HOST = '127.0.0.1'
        o.MYSQL_PORT = 3306
        o.MYSQL_USER = 'work'
        o.MYSQL_PASSWD = '42qu'
        o.MYSQL_DB = 'work_notepad'
    else:
        #o.DEBUG = False 
        o.DEBUG = True 
        o.MYSQL_HOST = sae.const.MYSQL_HOST 
        o.MYSQL_PORT = int(sae.const.MYSQL_PORT)
        o.MYSQL_USER = sae.const.MYSQL_USER 
        o.MYSQL_PASSWD = sae.const.MYSQL_PASS
        o.MYSQL_DB = sae.const.MYSQL_DB 


    from render import render
    o.render = render

def post_config(o):
    o.HOST_CSS_JS = 's.%s'%o.HOST

#    o.URL_CSS_JS = '//%s'%o.HOST_CSS_JS

