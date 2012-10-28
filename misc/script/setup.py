#!/usr/bin/env python
#coding:utf-8
from setuptools import setup, find_packages 

setup(
    name='cc42',
    version="0.0.1",
    description= """
            A paste tool of CLI
        1.Paste file to 42qucc
          hi@Mars ~$ 42cc < foo.txt  
          http://42qu.cc/xa47qt471
        2.Custom url 
          hi@Mars ~$ 42qucc hi < foo.txt
          http://42qu.cc/hi
        3.Save web page to local file
          hi@Mars ~$ 42cc  http://42qu.cc/xa47qt471  >  foo.txt
        """,
    author="42qu.com 42区",
    author_email="admin@42qu.com",
    url="http://42qu.cc/:help",
    packages = ['cc42'],
    zip_safe=False,
    include_package_data=True,
    install_requires = [
        'requests>=0.13.3',
    ],
    entry_points = {
        'console_scripts': [
            'cc42=cc42.cc42:main',
        ],
    },

)

if __name__ == "__main__":
    import sys
    if sys.getdefaultencoding() == 'ascii':
        reload(sys)
        sys.setdefaultencoding('utf-8')

