#coding:utf-8
import _env
from tornado import web
from config import render

class View(web.RequestHandler):
    def render(self, template_name=None, **kwds):
        kwds['request'] = self.request
        kwds['this'] = self
        if not self._finished:
            self.finish(render(template_name, **kwds))

