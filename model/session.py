#coding:utf-8

import time
import string
import uuid
from model._db import kv

key = 'address'

def session_new(user_id):
    s = str(uuid.uuid4()).replace('-', '')
    kv.set(s, user_id)
    return s

def user_id_by_session(s):
    return kv.get(s)

def session_rm(s):
    kv.set(s, '')

if __name__ == "__main__":
    pass
