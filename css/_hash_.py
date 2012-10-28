#coding:utf-8

import _env

__HASH__ =  {
    "index.css" : 'qTMnS3GxpD9Dx12nLVX1eQ.css', #index
    "base.css" : 'dEnughKoGCBkAXRcphq2pg.css', #base
    "reset.css" : '2e3_01C9IYVx_RQanGWNKQ.css', #reset
    "history.css" : 'rrZnoVUtN7gZflrmv5NOdw.css', #history
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
                            
