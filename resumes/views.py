from pyramid.view import view_config
from pyramid_sqlalchemy import Session as db
from .models import (
    Resume,
    CVItemCategories,
    CVListItemCategories,
    ItemCategories,
    CVListItem,
    CVItems,
    CVListHeading,
    CVColumns,
    CVColumnGroup,
    CVEntry,
    Section,
    Person,
    Address,
    Phone)
from resumes.forms import route_form
from authorize import login


def get_items(clazz, userid):
    objs = db.query(clazz).filter(clazz.user_id == userid)
    return objs.filter(clazz.logical_del.isnot(1))


@view_config(route_name='front_page',
             renderer='templates/home.jinja2')
def home_page(request):
    if 'form.submitted' in request.params and request.params['form.submitted'] == 'Login':
        return login(request)
    return dict(user=request.authenticated_userid)


@view_config(route_name='edit_items',
             renderer='templates/edit_items.jinja2',
             permission='view')
def edit_items(request):
    if request.method == 'POST':
        form_name = request.params['form_name']
        return route_form(form_name, request)

    user = request.authenticated_userid

    cvitems = sorted(get_items(CVItems, user).all(),
                     key=lambda x: x.text)
    cvlistitems = sorted(get_items(CVListItem, user).all(),
                         key=lambda x: x.text)
    categories = sorted(get_items(ItemCategories, user).all(),
                        key=lambda x: x.label)

    return dict(user=user,
                short_items=cvitems,
                long_items=cvlistitems,
                categories=categories)


@view_config(route_name='view_resume',
             renderer='templates/view_resume.jinja2',
             permission='view')
def view_resume(request):

    user = request.authenticated_userid
    resumes = get_items(Resume, user).all()

    return dict(user=user,
                resumes=resumes)


@view_config(route_name='select_template',
             renderer='templates/select_template.jinja2',
             permission='view')
def select_template(request):
    user = request.authenticated_userid
    return dict(user=user)


@view_config(route_name='select_resume',
             renderer='templates/select_resume.jinja2',
             permission='view')
def select_resume(request):

    user = request.authenticated_userid
    resumes = get_items(Resume, user).all()

    return dict(user=user,
                resumes=resumes)


@view_config(route_name='edit_resume',
             renderer='templates/edit_resume_casual.jinja2',
             permission='view')
def edit_resume(request):

    resume_id = request.matchdict['resume_id']
    user = request.authenticated_userid
    resume = get_items(Resume, user).filter(Resume.id == resume_id).all()
    if resume:
        if len(resume) > 1:
            raise Exception
        else:
            return dict(resume=resume[0],
                        user=user)
    else:
        message = 'Resume not found'
        return dict(message=message,
                    user=user)


@view_config(route_name='edit_resume_form',
             renderer='templates/edit_resume_form.jinja2',
             permission='view')
def resume_edit_forms(request):
    return dict()
