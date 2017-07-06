=========
ResumeApp
=========
Introduction
------------

This app is for building a resume in a highly structured way.  Other editors I have seen allow too much free-form text which decreases programatic manipulation.  The idea is to break a resume down into sections which allow for maximum re-use across resumes.  For example, almost all resumes have sections like Education, Experience, etc, which have a similar heading containing years experienced, location, title, etc.  What's under the sections depends on what a candidate wa
nts to emphesize.
Structuring the content this way, templates can be easily used to give the resume different looks, and as output engines are added, can give doc, pdf, and web representations.

Functionality
-------------
- Sections and section headings
- Long form, cohesive statements which represent section introductions, intentded for paragraph length
- Sentence length items, meant to be added, moved, or removed as a single thought
- Adding keywords for sections that are lists, i.e. skills, accolades, etc.  highly resuable
- Output to html and pdf via LaTeX


Technical Details
-----------------
- Pyramid drives the app
- SQLAlchemy as the ORM 
- Jinja2 as the templating engine
- JQuery JavaScript lib and
- selenium is used in some testing.

resumes/scripts/resumes.js is the JavaScript that I personally wrote
