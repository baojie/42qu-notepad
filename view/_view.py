#coding:utf-8
import _env
import json
from tornado import web
from config import render
from model.session import session_new, session_rm, user_id_by_session
import css, js
from model._db import mc

class View(web.RequestHandler):
    def render(self, template_name=None, **kwds):
        kwds['request'] = self.request
        kwds['this'] = self
        kwds['css'] = css
        kwds['js'] = js
        if not self._finished:
            self.finish(render(template_name, **kwds))

    def on_finish(self):
        mc.reset()

    @property
    def user_id(self):
        s = self.get_cookie('S')
        if s:
            user_id = user_id_by_session(s)
            if not user_id:
                self.clear_cookie('S')
            else:
                return user_id
        return 0

class LoginView(View):
    def prepare(self):
        super(LoginView, self).prepare()
        if not self.user_id:
            self.redirect('/signin')

def login(self, user_id):
    user_id = int(user_id)
    session = session_new(user_id)
    self.set_cookie('S', session)

def logout(self):
    s = self.get_cookie('S')
    session_rm(s)
    self.clear_cookie('S')
    
