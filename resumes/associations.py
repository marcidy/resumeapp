from sqlalchemy import (Column,
                        Integer,
                        ForeignKey,
                        Table,)
from pyramid_sqlalchemy import BaseObject as Base


itemized_lists_table = Table('itemized_lists',
                             Base.metadata,
                             Column('cvlist_id',
                                    Integer,
                                    ForeignKey('cvlistitems.id')),
                             Column('cvlisthead_id',
                                    Integer,
                                    ForeignKey('cvlistheadings.id')))


column_items_table = Table('cvcolumn_items',
                           Base.metadata,
                           Column('cvcolumns_id',
                                  Integer,
                                  ForeignKey('cvcolumns.id')),
                           Column('column_item_id',
                                  Integer,
                                  ForeignKey('cvitems.id')))


group_column_table = Table('grouped_columns',
                           Base.metadata,
                           Column('group_id',
                                  Integer,
                                  ForeignKey('cvcolumngroup.id')),
                           Column('cvcolumn_id',
                                  Integer,
                                  ForeignKey('cvcolumns.id')))


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


resume_section_table = Table('resume_sections',
                             Base.metadata,
                             Column('resume_id',
                                    Integer,
                                    ForeignKey('resumes.id')),
                             Column('section_id',
                                    Integer,
                                    ForeignKey('cvsection.id')))


cvitem_category_table = Table('cvitem_categories',
                              Base.metadata,
                              Column('cvitem_id',
                                     Integer,
                                     ForeignKey('cvitems.id')),
                              Column('category_id',
                                     Integer,
                                     ForeignKey('cvitemcategories.id')))


cvlistitem_category_table = Table('cvlistitem_categories',
                                  Base.metadata,
                                  Column('cvlistitem_id',
                                         Integer,
                                         ForeignKey('cvlistitems.id')),
                                  Column('category_id',
                                         Integer,
                                         ForeignKey('cvitemcategories.id')))
