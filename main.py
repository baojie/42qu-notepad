#coding:utf-8

from handler import Handler
from random import choice
from config import connection
from time import time

URL_ENCODE = 'abcdefghijklmnopqrstuvwxyz0123456789'


class HandlerIndex(Handler):
    def get(self, url):
        if not url:
            url = ''.join(choice(URL_ENCODE) for i in xrange(9))
            self.redirect(url)
        else:
            url = url.lower()
            cursor = connection.cursor()
            cursor.execute('select txt from notepad where url=%s', url)
            txt = cursor.fetchone()
            if txt:
                txt = txt[0]
            else:
                txt = ''
            self.render('/index.html', txt=txt)

    def post(self, url):
        if url:
            url = url.lower()
            txt = self.get_argument('txt', False)
            now = time()
            cursor.execute("insert into notepad (url,txt,`time`) values (%s,%s,%s) ON DUPLICATE KEY UPDATE txt=%s,`time`=%s", (url,txt,now,txt,now))
        self.finish({'time':now})

import tornado.web
application = tornado.web.Application([
    (r"/([a-zA-Z0-9]*)", HandlerIndex),
])

if __name__ == '__main__':
    import tornado.ioloop
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


