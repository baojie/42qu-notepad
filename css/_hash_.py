#coding:utf-8

import _env

__HASH__ =  {
    "base.css" : 'dEnughKoGCBkAXRcphq2pg.css', #base
    "history.css" : 'Ic-WsmoYNELykzvFO3pIUg.css', #history
    "reset.css" : '4yUW2pgRTE8SngskVbqJRQ.css', #reset
    "index.css" : 'r32onSxdK2Ra7DuRSbCWcg.css', #index
}


from config import DEBUG, HOST, HOST_CSS_JS
from os.path import dirname,basename
__vars__ = vars()

for file_name, hash in __HASH__.iteritems():
    
    if DEBUG:
        value = "http://%s/%s/%s"%(HOST, basename(dirname(__file__)),   file_name)
    else:
        value = "http://%s/build/%s"%(HOST_CSS_JS, hash) 
    
    name = file_name.rsplit('.', 1)[0].replace('.', '_').replace('-', '_').replace('/', '_')
    
    __vars__[name] = value
                            
