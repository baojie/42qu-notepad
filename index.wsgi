import _env
import tornado.web
from tornado.httpclient import AsyncHTTPClient
import view._url
from view._route import route

from config import DEBUG 
 
settings = {
    "debug": DEBUG,
}
application = tornado.web.Application(route.handlers, **settings)
