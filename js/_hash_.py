#coding:utf-8

import _env

__HASH__ =  {
    "base.js" : 'xVbfwK4lLRAPjYMx5ldWmg.js', #base
    "index.js" : 'gfzrHp0nAE4EqKlsaYHj0g.js', #index
    "history.js" : 'YcEURnXkaAG2dvZs_XNkag.js', #history
    "paging.js" : 'HV6PX0oDIW5R2pqlIMActw.js', #paging
    "ext.js" : 'fYbDzFtJEhehMZhJPy1i6Q.js', #ext
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
                            
