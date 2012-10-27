#coding:utf-8

import tornado.web
from config import DEBUG
from view.index import ViewIndex, SignIndex, History, GoogleHandler

application = tornado.web.Application(
    [
        (r"/signin", SignIndex),
        (r"/history", History),
        (r"/oauth", GoogleHandler),
        (r"/(.*)", ViewIndex),
    ],
    debug=DEBUG
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
