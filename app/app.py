import os

from pyramid.config import Configurator
from waitress import serve

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.add_static_view(name='static', path='../static/')
        config.add_route('root', '/')
        config.scan('views')

        app = config.make_wsgi_app()

    serve(app, host='0.0.0.0', port=port)
