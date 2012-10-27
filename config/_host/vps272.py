
#coding:utf-8

def pre_config(o):
    o.HOST = '42qu.me'
    o.MYSQL_USER = 'work'
    o.MYSQL_PASSWD = '42qu'
    o.DEBUG = True
    pass

def post_config(o):
    o.HOST_CSS_JS = 's.%s'%o.HOST

