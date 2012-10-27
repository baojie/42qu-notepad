#coding:utf-8

import _env
import time
import urllib
import tornado.web
import tornado.auth
from _view import View, JsonView
from model.index import gen_url, save_txt, txt_by_url
from model.account import account_new


class ViewIndex(JsonView):
    def get(self):
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

