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


def get_items(clazz):
    return db.query(clazz).filter(clazz.logical_del.isnot(1))


@view_config(route_name='edit_items', renderer='templates/edit_items.jinja2')
def edit_items(request):
    if request.method == 'POST':
        form_name = request.params['form_name']
        return route_form(form_name, request)

    cvitems = sorted(get_items(CVItems).all(),
                     key=lambda x: x.text)
    cvlistitems = sorted(get_items(CVListItem).all(),
                         key=lambda x: x.text)
    categories = sorted(get_items(ItemCategories).all(),
                        key=lambda x: x.label)

    return dict(short_items=cvitems,
                long_items=cvlistitems,
                categories=categories)
