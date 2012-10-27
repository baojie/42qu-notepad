#coding:utf-8

import sys
from os.path import dirname, abspath, exists, join
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')



def _():
    PREFIX = dirname(abspath(__file__))
    PWD = abspath(__file__)
    while True and len(PWD) > 1:
        PWD = dirname(PWD)
        if exists('%s/model'%PWD) and exists('%s/lib'%PWD) and exists('%s/view'%PWD):
            PREFIX = PWD
    if PREFIX and PREFIX not in sys.path:
        sys.path.insert(0, PREFIX)



_()
