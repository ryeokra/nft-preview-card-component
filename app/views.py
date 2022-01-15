from html import escape

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='root', renderer='../templates/index.jinja2')
def root_view(request):
    return {'hi': 'Welcome'}
