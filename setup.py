import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()

requires = [
    'Paste',
    'alembic',
    'bcrypt',
    'jinja2',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'pyramid_sqlalchemy',
    'SQLAlchemy',
    'selenium',
    'transaction',
    'waitress',
    'zope.sqlalchemy',
]
setup(name='resumes',
      version='0.1',
      description='resumes',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Matthew Arcidy',
      author_email='marcidy@arcidy.com',
      url='arcidy.com',
      keywords='resume latex jinja2',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='resumes',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = resumes:main
      """,
      )
