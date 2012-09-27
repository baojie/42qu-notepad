#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from os.path import dirname, abspath, exists, join
from mako.lookup import TemplateLookup


DEBUG = True
PREFIX = dirname(abspath(__file__))

_lookup = TemplateLookup(
    directories=join(PREFIX, 'html'),
    module_directory='/tmp/mako',
    disable_unicode=True,
    encoding_errors='ignore',
    default_filters=['str', 'h'],
    filesystem_checks=DEBUG,
    input_encoding='utf-8',
    output_encoding=''
)


def render(html, **kwds):
    return _lookup.get_template(html).render(**kwds)

