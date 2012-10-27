import _env
import tornado.web
from tornado.httpclient import AsyncHTTPClient
from view.index import ViewIndex
 
 
settings = {
    "debug": True,
}
 
# application should be an instance of `tornado.web.Application`,
# and don't wrap it with `sae.create_wsgi_app`
application = tornado.web.Application([
    (r"/", ViewIndex),
], **settings)
