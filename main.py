#coding:utf-8

from handler import Handler

class HandlerIndex(Handler):
    def get(self):
        self.render()


import tornado.web
application = tornado.web.Application([
    (r"/", HandlerIndex),
])

if __name__ == '__main__':
    import tornado.ioloop
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


