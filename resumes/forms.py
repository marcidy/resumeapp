from pyramid.httpexceptions import HTTPFound
from pyramid_sqlalchemy import Session as db
from resumes.models import (CVItems,
                            CVListItem,
                            ItemCategories)
import transaction


def came_from(request):
    referrer = request.url
    came_from = request.params.get('came_from', referrer)
    return HTTPFound(location=came_from)


def new_item(clazz, request):
    text = request.params['text']
    username = request.authenticated_userid()
    item = clazz(text=text, user_id=username)
    with transaction.manager:
        db.add(item)

    return came_from(request)


def delete_items(clazz, items):
    to_delete = db.query(clazz).filter(clazz.id.in_(items)).all()
    map(lambda x: setattr(x, 'logical_del', 1), to_delete)

    with transaction.manager:
        db.add_all(to_delete)


def filter_checked(items, by_key_string):
    item_list = [int(item.strip(by_key_string))
                 for item, value in items.iteritems()
                 if by_key_string in item and value == 'on']
    return item_list


def delete_short_item(request):
    short_list = filter_checked(request.params, "short_")
    delete_items(CVItems, short_list)
    return came_from(request)


def delete_long_item(request):
    long_list = filter_checked(request.params, "long_")
    delete_items(CVListItem, long_list)
    return came_from(request)


def delete_category_item(request):
    cat_list = filter_checked(request.params, "category_")
    delete_items(ItemCategories, cat_list)
    return came_from(request)


def new_short_item(request):
    return new_item(CVItems, request)


def new_long_item(request):
    return new_item(CVListItem, request)


def new_category(request):
    username = request.authenticated_userid()
    label = request.params['label']
    cat = ItemCategories(label=label,
                         user_id=username)

    with transaction.manager:
        db.add(cat)

    return came_from(request)


def route_form(form_name, request):
    return FORM_REGISTER[form_name](request)


FORM_REGISTER = dict(new_short_item=new_short_item,
                     new_long_item=new_long_item,
                     delete_short_item=delete_short_item,
                     delete_long_item=delete_long_item,
                     new_category=new_category,
                     delete_category_item=delete_category_item)
