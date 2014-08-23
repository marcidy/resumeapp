from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from resumes.authorize import groupfinder


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application.
    """
    authn_policy = AuthTktAuthenticationPolicy(
        '89bdd8b12bc342b79f4e817646f8e206',
        callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings,
                          root_factory='resumes.authorize.RootFactory')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.include('pyramid_jinja2')
    config.include('pyramid_tm')
    config.include('pyramid_sqlalchemy')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('scripts', 'scripts')
    config.add_route('front_page', '/')
    config.add_route('edit_items', '/items/edit')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('register', '/register')
    config.add_route('view_resume', '/resumes/view')
    config.add_route('select_template', '/resumes/new')
    config.add_route('select_resume', '/resumes/select')
    config.add_route('edit_resume', '/resumes/{resume_id}/edit')
    config.add_route('edit_resume_form', '/forms/resume_edit')
    config.scan(ignore="resumes.scripts.test_selenium")
    return config.make_wsgi_app()
