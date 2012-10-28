#coding:utf-8

import _env

__HASH__ =  {
    "base.js" : 'xVbfwK4lLRAPjYMx5ldWmg.js', #base
    "index.js" : 'MVD361eEnY8QtCDZNSCOzw.js', #index
    "history.js" : 'ZtF9rnfvx9KkjZM8xL2ulw.js', #history
    "paging.js" : '1TrgtxyZArTan_qlNLy9mA.js', #paging
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
                            
