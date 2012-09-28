#coding:utf-8

from handler import Handler
from random import choice

URL_ENCODE = 'abcdefghijklmnopqrstuvwxyz0123456789'


class HandlerIndex(Handler):
    def get(self, url):
        if not url:
            url = ''.join(choice(URL_ENCODE) for i in xrange(9))
            self.redirect(url)
        else:
            self.render('/index.html')

    def post(self, url):
        self.finish('{}')

import tornado.web
application = tornado.web.Application([
    (r"/([a-zA-Z0-9]*)", HandlerIndex),
])

if __name__ == '__main__':
    import tornado.ioloop
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


