#coding:utf-8
import _env
from tornado import web
from config import render
from model.session import session_new, user_id_by_session

class View(web.RequestHandler):
    def render(self, template_name=None, **kwds):
        kwds['request'] = self.request
        kwds['this'] = self
        if not self._finished:
            self.finish(render(template_name, **kwds))

    @property
    def user_id(self):
        s = self.get_cookie('S')
        if s:
            user_id = user_id_by_session(s)
            if not user_id:
                self.clear_cookie('S')
            else:
                return user_id


def login(user_id):
    user_id = int(user_id)
    session = session_new(user_id)
    self.set_cookie('S', session)
