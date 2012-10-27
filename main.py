#coding:utf-8

import tornado.web
from config import DEBUG
from view.index import ViewIndex

application = tornado.web.Application(
    [
        (r"/(.*)", ViewIndex),
    ],
    debug=DEBUG
)

if __name__ == '__main__':
    import sys
    import tornado.ioloop
    if len(sys.argv)>1:
        port = sys.argv[1]
    else:
        port = 8888
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()


