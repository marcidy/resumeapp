import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()

requires = [
    'jinja2',
    'sqlalchemy',
    'alembic',
    'transaction',
]
setup(name='resumes',
      version='0.0',
      description='resumes',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
      ],
      author='',
      author_email='',
      url='',
      keywords='resume latex jinja2',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='resumes',
      install_requires=requires,
      )
