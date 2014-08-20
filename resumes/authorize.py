from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
)
from pyramid.httpexceptions import HTTPFound, HTTPInternalServerError
from pyramid.security import (
    remember,
    forget,
    Allow,
    Authenticated,
    Everyone,
    Deny,
    DENY_ALL,
    ALL_PERMISSIONS)
from pyramid_sqlalchemy import Session as db
from pyramid_sqlalchemy import BaseObject as Base
from pyramid.view import view_config, forbidden_view_config
import bcrypt


class RootFactory(object):
    __acl__ = [(Allow, Everyone, 'home'),
               (Allow, Authenticated, 'view'),
               (Allow, 'g:admin', ALL_PERMISSIONS), ]

    def __init__(self, request):
        pass


class User(Base):
    """ clients, contributors, moderators, etc """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(Text, unique=True)
    password = Column(Text)
    salt = Column(Text)

    def check_password(self, passwd):
        hashed = bcrypt.hashpw(str(passwd), str(self.salt))
        return hashed == self.password


def get_user(userid):
    try:
        found = db.query(User).filter_by(username=userid).one()
    except:
        return None
    else:
        return found


class Group(Base):
    ''' groups to which users belong '''
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    user = Column(Integer, ForeignKey('users.id'))


def groupfinder(userid, request):
    found = get_user(userid)
    if found:
        groups = db.query(Group).filter_by(user=found.id).all()
    return groups


@view_config(route_name='login', renderer='templates/login.jinja2')
@forbidden_view_config(renderer='templates/login.jinja2')
def login(request):
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/'

    came_from = request.params.get('came_from', referrer)
    message = ''
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        user = db.query(User).filter_by(username=login)
        if user.count() == 0:
            message = 'Login Failed'
        elif user.count() == 1:
            user = user.one()
            if user and user.check_password(password):
                headers = remember(request, login)
                return HTTPFound(location=came_from,
                                 headers=headers)
        else:
            return HTTPInternalServerError()
        message = 'Login Failed'

    return dict(message=message,
                url=request.application_url + '/login',
                came_from=came_from,
                login=login,
                password=password)


@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('front_page'),
                     headers=headers)


@view_config(route_name='register', renderer='templates/register.jinja2')
def register(request):
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/'
    came_from = request.params.get('came_from', referrer)
    message = ''
    login = ''
    password = ''
    reg_url = request.route_url('register')

    if 'form.submitted' in request.params:
        fail = False
        login = request.params['login']
        password = request.params['password'].encode('utf-8')
        passwd_ck = request.params['password_check'].encode('utf-8')

        if password != passwd_ck:
            message = '\nPasswords do not match'
            fail = True

        user = db.query(User).filter_by(username=login).all()

        if user:
            message += '\nUsername already exists'
            fail = True

        if fail:
            return dict(message=message,
                        url=reg_url,
                        came_from=came_from,
                        login=login)
        if not user and not fail:
            salt = bcrypt.gensalt()
            user = User(username=login,
                        password=bcrypt.hashpw(password, salt),
                        salt=salt)
            db.add(user)
            return HTTPFound(location=request.route_url('login'))

    return dict(message=message,
                login=login,
                password='',
                url=reg_url,
                came_from=came_from)
