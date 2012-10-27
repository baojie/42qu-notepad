#coding:utf-8

from config import DEBUG
import tornado.web
import view._url
from view._route import route

application = tornado.web.Application(
    route.handlers,
    debug=DEBUG,
#    [
#        (r"/signin", SignIndex),
#        (r"/history", History),
#        (r"/oauth", GoogleHandler),
#        (r"/(.*)", ViewIndex),
#    ],
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
