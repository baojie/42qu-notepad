#coding:utf-8

import _env

__HASH__ =  {
    "base.css" : 'dEnughKoGCBkAXRcphq2pg.css', #base
    "history.css" : '9Y1MDtH2O0fPmpz4lsGFlg.css', #history
    "reset.css" : '4yUW2pgRTE8SngskVbqJRQ.css', #reset
    "index.css" : 'vEWFegO-5PjMkjQxyUFdhQ.css', #index
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
                            
