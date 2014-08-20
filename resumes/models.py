from pyramid_sqlalchemy import BaseObject as Base
from sqlalchemy import (Column,
                        Text,
                        Integer,
                        String,
                        ForeignKey,)
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship
from resumes.associations import (itemized_lists_table,
                                  column_items_table,
                                  group_column_table,
                                  entry_items_table,
                                  entry_columns_table,
                                  entry_itemized_table,
                                  section_entry_table,
                                  section_items_table,
                                  section_columngroup_table,
                                  section_itemized_table,
                                  resume_section_table,
                                  cvitem_category_table,
                                  cvlistitem_category_table,
                                  )


class Common(object):
    logical_del = Column(Integer)

    @declared_attr
    def user_id(cls):
        return Column(Integer, ForeignKey('users.id'))


class Person(Base, Common):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    email = Column(Text)
    linkedin = Column(Text)
    twitter = Column(Text)
    facebook = Column(Text)
    address = relationship("Address", uselist=False, backref="person")
    phone = relationship("Phone")
    resumes = relationship("Resume", backref="person")


class Address(Base, Common):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    street_num = Column(Integer)
    street_name = Column(Text)
    street_type = Column(Text)
    apt_num = Column(Text)
    city = Column(Text)
    state = Column(Text)
    zip = Column(Integer)


class Phone(Base, Common):
    __tablename__ = 'phone'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    type = Column(Text)
    country = Column(Integer)
    area_code = Column(Integer)
    prefix = Column(Integer)
    line_number = Column(Integer)


class ItemCategories(Base, Common):
    __tablename__ = 'cvitemcategories'
    id = Column(Integer, primary_key=True)
    label = Column(Text)
    type = Column(String(20))

    __mapper_args__ = {
        'polymorphic_on': type,
    }


class CVItemCategories(ItemCategories):
    __mapper_args__ = {
        'polymorphic_identity': 'CVItem'
    }


class CVListItemCategories(ItemCategories):
    __mapper_args__ = {
        'polymorphic_identity': 'CVListItem'
    }


class CVListItem(Base, Common):

    ''' Long description items '''
    __tablename__ = 'cvlistitems'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    categories = relationship('CVListItemCategories',
                              secondary=cvlistitem_category_table,
                              backref='cvlistitems')


class CVItems(Base, Common):

    ''' short description items, like a skill '''
    __tablename__ = 'cvitems'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    categories = relationship('CVItemCategories',
                              secondary=cvitem_category_table,
                              backref='cvitems')


class CVListHeading(Base, Common):
    __tablename__ = 'cvlistheadings'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    items = relationship("CVListItem",
                         secondary=itemized_lists_table)


class CVColumns(Base, Common):
    __tablename__ = 'cvcolumns'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    items = relationship("CVItems",
                         secondary=column_items_table)


class CVColumnGroup(Base, Common):
    __tablename__ = 'cvcolumngroup'
    id = Column(Integer, primary_key=True)
    cvcolumns = relationship("CVColumns",
                             secondary=group_column_table)


class CVEntry(Base, Common):
    __tablename__ = 'cventry'
    id = Column(Integer, primary_key=True)
    start_yr = Column(Integer)
    end_yr = Column(Integer)
    title = Column(Text)
    institution = Column(Text)
    city = Column(Text)
    state = Column(Text(2))
    gpa = Column(Text)
    honors = Column(Text)
    description = Column(Text)
    cvlistitems = relationship('CVListItem',
                               secondary=entry_items_table)
    cvcolumns = relationship('CVColumns',
                             secondary=entry_columns_table)
    cvitemized = relationship('CVListHeading',
                              secondary=entry_itemized_table)


class Section(Base, Common):

    ''' Structure the sections:
        section
          + description
          + cventry
            + cvlistitems
            + cvcolumns
              + cvitems
            + list heading
              + list items
          + cvlistitems
          + cvcolumns
            + cvitems
          + list heading
            + list items
        '''
    __tablename__ = 'cvsection'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    cventry = relationship('CVEntry',
                           secondary=section_entry_table)
    cvlistitems = relationship('CVListItem',
                               secondary=section_items_table)
    cvcolumngroups = relationship('CVColumnGroup',
                                  secondary=section_columngroup_table)
    cvitemized = relationship('CVListHeading',
                              secondary=section_itemized_table)


class Resume(Base, Common):
    __tablename__ = 'resumes'
    id = Column(Integer, primary_key=True)
    style = Column(Text)
    color = Column(Text)
    title = Column(Text)
    footnotestyle = Column(Text)
    person_id = Column(Integer, ForeignKey('person.id'))
    sections = relationship("Section",
                            secondary=resume_section_table)

    def ft_symbols(self):
        str = r'\renewcommand{\thefootnote}{\fnsymbol{footnote}}'
        return str
