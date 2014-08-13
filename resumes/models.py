from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column,
                        Text,
                        Integer,
                        ForeignKey,
                        Table,)
from sqlalchemy.orm import relationship

Base = declarative_base()


class Person(Base):
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


class Address(Base):
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


class Phone(Base):
    __tablename__ = 'phone'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    type = Column(Text)
    country = Column(Integer)
    area_code = Column(Integer)
    prefix = Column(Integer)
    line_number = Column(Integer)


class CVItemCategories(Base):
    __tablename__ = 'cvitemcategories'
    id = Column(Integer, primary_key=True)
    label = Column(Text)

itemized_lists_table = Table('itemized_lists',
                             Base.metadata,
                             Column('cvlist_id',
                                    Integer,
                                    ForeignKey('cvlistitems.id')),
                             Column('cvlisthead_id',
                                    Integer,
                                    ForeignKey('cvlistheadings.id')))


class CVListItem(Base):

    ''' Long description items '''
    __tablename__ = 'cvlistitems'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
#    categories = relationship('CVItemCategories')


column_items_table = Table('cvcolumn_items',
                           Base.metadata,
                           Column('cvcolumns_id',
                                  Integer,
                                  ForeignKey('cvcolumns.id')),
                           Column('column_item_id',
                                  Integer,
                                  ForeignKey('cvitems.id')))


class CVItems(Base):

    ''' short description items, like a skill '''
    __tablename__ = 'cvitems'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
#    categories = relationship('CVItemCategories')


class CVListHeading(Base):
    __tablename__ = 'cvlistheadings'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    items = relationship("CVListItem",
                         secondary=itemized_lists_table)


class CVColumns(Base):
    __tablename__ = 'cvcolumns'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    items = relationship("CVItems",
                         secondary=column_items_table)


group_column_table = Table('grouped_columns',
                           Base.metadata,
                           Column('group_id',
                                  Integer,
                                  ForeignKey('cvcolumngroup.id')),
                           Column('cvcolumn_id',
                                  Integer,
                                  ForeignKey('cvcolumns.id')))


class CVColumnGroup(Base):
    __tablename__ = 'cvcolumngroup'
    id = Column(Integer, primary_key=True)
    cvcolumns = relationship("CVColumns",
                             secondary=group_column_table)


entry_items_table = Table('entry_items',
                          Base.metadata,
                          Column('entry_id',
                                 Integer,
                                 ForeignKey('cventry.id')),
                          Column('item_id',
                                 Integer,
                                 ForeignKey('cvlistitems.id')))


entry_columns_table = Table('entry_columns',
                            Base.metadata,
                            Column('entry_id',
                                   Integer,
                                   ForeignKey('cventry.id')),
                            Column('cvcolumns_id',
                                   Integer,
                                   ForeignKey('cvcolumns.id')))


entry_itemized_table = Table('entry_itemized',
                             Base.metadata,
                             Column('entry_id',
                                    Integer,
                                    ForeignKey('cventry.id')),
                             Column('cvitemized_id',
                                    Integer,
                                    ForeignKey('cvlistheadings.id')))


class CVEntry(Base):
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


section_entry_table = Table('section_entry',
                            Base.metadata,
                            Column('section_id',
                                   Integer,
                                   ForeignKey('cvsection.id')),
                            Column('entry_id',
                                   Integer,
                                   ForeignKey('cventry.id')))


section_items_table = Table('section_items',
                            Base.metadata,
                            Column('section_id',
                                   Integer,
                                   ForeignKey('cvsection.id')),
                            Column('item_id',
                                   Integer,
                                   ForeignKey('cvlistitems.id')))


section_columngroup_table = Table('section_columngroupss',
                                  Base.metadata,
                                  Column('section_id',
                                         Integer,
                                         ForeignKey('cvsection.id')),
                                  Column('cvcolumngroups_id',
                                         Integer,
                                         ForeignKey('cvcolumngroup.id')))


section_itemized_table = Table('section_itemized',
                               Base.metadata,
                               Column('section_id',
                                      Integer,
                                      ForeignKey('cvsection.id')),
                               Column('cvitemized_id',
                                      Integer,
                                      ForeignKey('cvlistheadings.id')))


class Section(Base):

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


resume_section_table = Table('resume_sections',
                             Base.metadata,
                             Column('resume_id',
                                    Integer,
                                    ForeignKey('resumes.id')),
                             Column('section_id',
                                    Integer,
                                    ForeignKey('cvsection.id')))


class Resume(Base):
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
