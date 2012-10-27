#coding:utf-8
import _env
from os.path import join
from mako.lookup import TemplateLookup

from config import DEBUG
RENDER_PATH = [join(_env.PREFIX, 'html')]

template_lookup = TemplateLookup(
    directories=tuple(RENDER_PATH),
    #module_directory='/tmp/%s'%RENDER_PATH[0].strip('/').replace('/', '.'),
    disable_unicode=True,
    encoding_errors='ignore',
    default_filters=['str', 'h'],
    filesystem_checks=DEBUG,
    input_encoding='utf-8',
    output_encoding=''
)


def render(htm, **kwds):
    mytemplate = template_lookup.get_template(htm)
    return mytemplate.render(**kwds)
