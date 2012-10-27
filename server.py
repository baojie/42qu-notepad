#coding:utf-8

from config import DEBUG
import tornado.web
from view.index import ViewIndex, SignIndex, GoogleHandler

import view._url
from view._route import route

application = tornado.web.Application(
    route.handlers,
    debug=DEBUG,
)

def run():
    import sys
    import tornado.ioloop
    if len(sys.argv)>1:
        port = sys.argv[1]
    else:
        port = 8888
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    run()
