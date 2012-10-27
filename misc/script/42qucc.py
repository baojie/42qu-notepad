#!/usr/bin/env python
#coding:utf-8
import urllib
import requests 
import urllib2
import sys

HOST = 'pymo.sinaapp.com'
HOST_HTTP = 'http://%s'%HOST
API_URL = '%s//api'%HOST_HTTP


def post(url=''):
    data = ''.join(sys.stdin)
    r = requests.post(API_URL+"/set"+url, data={'txt':data}) 
    print r.text

def main():
    argv = sys.argv
    url = ''
    if len(argv) > 1:
        url = argv[1]
        if url.startswith(HOST_HTTP):
            url = url[len(HOST_HTTP):] 
            r = requests.get(API_URL+"/get"+url) 
            print r.text.rstrip()
            return
        else:
            url = argv[1]
            if url[0]!="/":
                url = "/"+url
    post(url)

if __name__ == '__main__':
    main()
