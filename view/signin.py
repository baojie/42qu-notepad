#coding:utf-8

import tornado.web
import tornado.auth
from _view import View
from model._db import connection


class GoogleHandler(tornado.web.RequestHandler, tornado.auth.GoogleMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
            user = self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Google auth failed")
        else:
            print 'user', type(user), user
            self.redirect('/')

class ViewIndex(View):
    def get(self, url):
        if not url:
            while True:
                url = ''.join(choice(URL_ENCODE) for i in xrange(9))
                if not txt_by_url(url):
                    break
            self.redirect(url)
        else:
            self.render('/index.html', txt=txt_by_url(url), url=url)

    def post(self, url):
        if url:
            url = url.lower()
            txt = self.get_argument('txt', '').rstrip()
            now = time()
            cursor = connection.cursor()
            if txt:
                cursor.execute(
                    'insert into notepad (url,txt,`time`) values '
                    '(%s,%s,%s) ON DUPLICATE KEY UPDATE txt=%s,`time`=%s',
                    (url, txt, now, txt, now)
                )
            else:
                cursor.execute('delete from notepad where url=%s', url)
        self.finish({'time':now})
