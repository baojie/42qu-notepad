#coding:utf-8
import _env
from misc.config._private.upyun import pre_config as pre_config_upyun 
from misc.config._private.pay import pre_config as pre_config_pay

def pre_config(o):
    pre_config_upyun(o)
    pre_config_pay(o)

def post_config(o):
    pass
