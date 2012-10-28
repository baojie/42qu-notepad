#!/usr/bin/env python
#coding:utf-8
from setuptools import setup, find_packages 

setup(
    name='42qucc',
    version="0.0.1",
    description="A paste tool of CLI",
    author="42qu.com 42区",
    author_email="admin@42qu.com",
    packages = ['42qucc'],
    zip_safe=False,
    include_package_data=True,
    install_requires = [
        'requests>=0.13.3',
    ],
    entry_points = {
        'console_scripts': [
            '42qucc=42qucc.qucc:main',
        ],
    },
)

if __name__ == "__main__":
    import sys
    if sys.getdefaultencoding() == 'ascii':
        reload(sys)
        sys.setdefaultencoding('utf-8')

