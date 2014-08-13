from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column,
                        Text,
                        Integer,
                        ForeignKey,)
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
    person = Column(Integer, ForeignKey('person.id'))
    type = Column(Text)
    country = Column(Integer)
    area_code = Column(Integer)
    prefix = Column(Integer)
    line_number = Column(Integer)


class CVItemCategories(Base):
    __tablename__ = 'cvitemcategories'
    id = Column(Integer, primary_key=True)
    label = Column(Text)


class CVListItem(Base):

    ''' Long description items '''
    __tablename__ = 'cvlistitems'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    categories = relationship('cvitemcategories')


class CVItems(Base):

    ''' short description items, like a skill '''
    __tablename__ = 'cvitems'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    categories = relationship('cvitemcategories')


class CVColumns(Base):
    __tablename__ = 'cvcolumns'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    items = relationship("CVItems")


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
    cvlistitems = relationship('cvlistitems')
    cvcolumns = relationship('cvcolumns')
    cvitemized = relationship('cvitems')


class Section(Base):

    ''' Structure the sections:
        section
          + cventry
            + cvlistitems
            + cvcolumns
            + itemized lists
        '''
    __tablename__ = 'cv_objects'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    cventry = relationship('cventry')


class Resume(Base):
    __tablename__ = 'resumes'
    id = Column(Integer, primary_key=True)
    style = Column(Text)
    color = Column(Text)
    title = Column(Text)
    footnotestyle = Column(Text)
    person_id = Column(Integer, ForeignKey('person.id'))
    sections = relationship("Sections")

    def ft_symbols(self):
        str = r'\renewcommand{\thefootnote}{\fnsymbol{footnote}}'
        return str
