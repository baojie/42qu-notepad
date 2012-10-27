#coding:utf-8

import _env
import time
import tornado.web
import tornado.auth
from _view import View, login
from model._db import connection
from model.index import gen_url, save_txt, txt_by_url
from model.account import account_new
from _route import route


class SignIndex(View):
    def get(self):
            self.render('/signin.html')

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
            name = user['name']
            email = user['email']
            user_id = account_new(name, email)
            login(self, user_id)
            self.redirect('/')

@route("/(.*)")
class ViewIndex(View):
    def get(self, url):
        print self.user_id
        if not url:
            url = gen_url()
            self.redirect(url)
        else:
            self.render('/index.html', txt=txt_by_url(url), url=url)

    def post(self, url):
        if url:
            url = url.lower()
            txt = self.get_argument('txt', '').rstrip()
            save_txt(url, txt)
        self.finish({'time':int(time.time())})
