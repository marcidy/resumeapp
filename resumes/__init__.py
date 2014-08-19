from pyramid.config import Configurator


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_tm')
    config.include('pyramid_sqlalchemy')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('scripts', 'scripts')
    config.add_route('front_page', '/')
    config.add_route('edit_items', '/items/edit')
    config.scan()
    return config.make_wsgi_app()
