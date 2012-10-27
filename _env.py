#coding:utf-8

import sys
from os.path import dirname, abspath, exists

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')




PREFIX = dirname(abspath(__file__))

if PREFIX and PREFIX not in sys.path:
    sys.path.insert(0, PREFIX)


