#!/usr/bin/env python
#coding:utf-8
import urllib
import requests 
import urllib2
import sys
import bz2

HOST = 'pymo.sinaapp.com'
HOST_HTTP = 'http://%s'%HOST
API_URL = '%s/:api'%HOST_HTTP

def help():
    print """
1.Paste file to 42qucc
  hi@Mars ~$ 42cc < foo.txt  
  http://42qu.cc/xa47qt471
2.Custom url 
  hi@Mars ~$ 42qucc hi < foo.txt
  http://42qu.cc/hi
3.Save web page to local file
  hi@Mars ~$ 42cc  http://42qu.cc/xa47qt471  >  foo.txt
    """

def post(url=''):
    data = ''.join(sys.stdin.readlines())
    print API_URL+url
    files = {'file': ('txt', bz2.compress(data) )}
    r = requests.post(API_URL+url, files=files, timeout=3)
    print r.text

def main():
    argv = sys.argv
    url = ''
    if len(argv) > 1:
        if len(argv) > 2:
            help()
            return
        url = argv[1]
        if url.startswith(HOST_HTTP):
            url = url[len(HOST_HTTP):] 
            r = requests.get(API_URL++url, timeout=3) 
            print r.text.rstrip()
            return
        else:
            url = argv[1]
            if url[0]!="/":
                url = "/"+url
    else:
        url = "/"+url

    post(url)

if __name__ == '__main__':
    main()
