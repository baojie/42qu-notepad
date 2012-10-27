#coding:utf-8

import time
import string
import uuid
from model._db import kv

key = 'address'

def session_new(user_id):
    db = kv()
    s = str(uuid.uuid4()).replace('-', '')
    db.set(s, user_id)
    return s

def user_id_by_session(s):
    db = kv()
    return db.get(s)

def session_rm(s):
    db = kv()
    db.set(s, '')

if __name__ == "__main__":
    pass
