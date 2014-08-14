import jinja2
import os
import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Resume


def init_db_from_config(config):
    sqlalchemy_url = config.get('database', 'sqlalchemy_url')
    engine = create_engine(sqlalchemy_url)
    session = sessionmaker(bind=engine)
    db = session()
    return db


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

    template = resume_renderer.get_template('./templates/resume-moderncv.tex')

    cv = db.query(Resume).all()[0]
    out = template.render(cv=cv)
    with open('testout.tex', 'w') as file:
        file.write(out)

if __name__ == '__main__':
    main()
