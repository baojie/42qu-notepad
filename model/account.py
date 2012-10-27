#coding:utf-8

import time
import string
from _db import connection


def account_new(username, email):
    username, email = map(string.strip, (username, email))
    if not user_id_by_email(email):
        cursor = connection.cursor()
        if email:
            cursor.execute(
                '''insert into `account` (name, email) values (%s,%s)''', (username, email)
            )
    

def user_id_by_email(email):
    cursor = connection.cursor()
    cursor.execute('select id from account where email=%s',email)
    user_id = cursor.fetchone()
    if user_id:
        user_id = user_id[0]
    else:
        user_id = 0
    return user_id

if __name__ == "__main__":
    account_new('Lerry', 'lerry@test.com')
    print user_id_by_email('lerry@test.com')
