#coding:utf-8

import _env

__HASH__ =  {
    "reset.css" : '4yUW2pgRTE8SngskVbqJRQ.css', #reset
    "history.css" : 'dz1pTmLBl2PxHHBYVXfBIg.css', #history
    "index.css" : 'FL0J2KpmnwFwzjUyEhy3RA.css', #index
    "base.css" : 'dEnughKoGCBkAXRcphq2pg.css', #base
    "help.css" : 'b4rnmKfIPNYONWS0TO5qyA.css', #help
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
                            
