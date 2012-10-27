#coding:utf-8

import _env

__HASH__ =  {
    "base.css" : 'ZRqkbXAIZACZJjuGvLmEcg.css', #base
    "index.css" : 'KT5NVqURYFW5bOtO1HyGCg.css', #index
    "reset.css" : '2e3_01C9IYVx_RQanGWNKQ.css', #reset
}


from config import DEBUG, HOST_CSS_JS, HOST_DEV_PREFIX
from os.path import dirname,basename
__vars__ = vars()

for file_name, hash in __HASH__.iteritems():
    
    if DEBUG:
        value = "http://%s%s%s/%s"%(HOST_DEV_PREFIX, basename(dirname(__file__)), HOST_CSS_JS,  file_name)
    else:
        value = "http://%s/%s"%(HOST_CSS_JS, hash) 
    
    name = file_name.rsplit('.', 1)[0].replace('.', '_').replace('-', '_').replace('/', '_')
    
    __vars__[name] = value
                           
 
