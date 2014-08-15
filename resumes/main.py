import jinja2
import os
import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Resume
import re


def init_db_from_config(config):
    sqlalchemy_url = config.get('database', 'sqlalchemy_url')
    engine = create_engine(sqlalchemy_url)
    session = sessionmaker(bind=engine)
    db = session()
    return db


LATEX_SUBS = (
    (re.compile(r'\\'), r'\\textbackslash'),
    (re.compile(r'([{}_#%&$])'), r'\\\1'),
    (re.compile(r'~'), r'\~{}'),
    (re.compile(r'\^'), r'\^{}'),
    (re.compile(r'"'), r"''"),
    (re.compile(r'\.\.\.+'), r'\\ldots'),
)


def escape_tex(value):
    newval = value
    for pattern, replacement in LATEX_SUBS:
        newval = pattern.sub(replacement, newval)
    return newval


def main():

    config = ConfigParser.RawConfigParser()
    config.read('../config.cfg')
    db = init_db_from_config(config)

    resume_renderer = jinja2.Environment(
        block_start_string='((*',
        block_end_string='*))',
        variable_start_string='(((',
        variable_end_string=')))',
        lstrip_blocks=True,
        trim_blocks=True,
        loader=jinja2.FileSystemLoader(os.path.abspath('.')))

    resume_renderer.filters['escape_tex'] = escape_tex

    template = resume_renderer.get_template('./templates/resume-moderncv.tex')

    cv = db.query(Resume).all()[0]
    out = template.render(cv=cv)
    with open('testout.tex', 'w') as file:
        file.write(out)


def html():

    config = ConfigParser.RawConfigParser()
    config.read('../config.cfg')
    db = init_db_from_config(config)

    resume_renderer = jinja2.Environment(
        block_start_string='((*',
        block_end_string='*))',
        variable_start_string='(((',
        variable_end_string=')))',
        lstrip_blocks=True,
        trim_blocks=True,
        loader=jinja2.FileSystemLoader(os.path.abspath('.')))

    template = resume_renderer.get_template('./templates/resume-moderncv.html')

    cv = db.query(Resume).all()[0]
    out = template.render(cv=cv)
    with open('testout.html', 'w') as file:
        file.write(out)

if __name__ == '__main__':
    html()
