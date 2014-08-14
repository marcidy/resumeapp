from resumes import models as md
from ConfigParser import RawConfigParser
from resumes.main import init_db_from_config
import transaction


def run():
    # import pdb
    # pdb.set_trace()
    config = RawConfigParser()
    config.read('./config.cfg')
    db = init_db_from_config(config)

    address = md.Address(street_num='28',
                         street_name='Sickles',
                         street_type='Street',
                         apt_num='A16',
                         city='New York City',
                         state='NY',
                         zip=10040)

    phone = md.Phone(type='mobile',
                     country=1,
                     area_code=508,
                     prefix=364,
                     line_number=7529)

    me = md.Person(first_name='Matthew',
                   last_name='Arcidy',
                   email='marcidy@gmail.com',
                   linkedin='www.linkedin.com/in/marcidy',
                   address=address,
                   phone=[phone])

    sections = []
    sections.append(md.Section(title='Objectives',
                               description=objectives))

    acs_list_items = [
        md.CVListItem(
            text='Design operation and business '
            'process for a Top 4 consulting firm\'s '
            'crowdsourcing unit, including work-flows '
            'and analytics'), md.CVListItem(
            text='Investigate and model statistical '
            'relationship between economic news events '
            'and volatility indices')]

    acs_corp = md.CVEntry(start_yr=2013,
                          title='Founder',
                          institution='Arcidy Computational Services',
                          city='New York City',
                          state='NY',
                          description='Provide consultation and innovation '
                          'services for any problems related to the function '
                          'and business of computation',
                          cvlistitems=acs_list_items)

    jpm_cvlist_items = [md.CVListItem(text='Develop, implement, and support '
                                      'systems for risk, profit and loss, and '
                                      'cash flow projection calculations')]

    jrm_items = [md.CVListItem(text='Lead change control for business '
                               'critical infrastructure'),
                 md.CVListItem(text='Organized transition from quarterly '
                               'release cycle to Continuous Integration'),
                 md.CVListItem(text='Prioritized git branches and merges')]
    jpm_rel_mgmt = md.CVListHeading(text='Release Management',
                                    items=jrm_items)

    jpdm_items = [md.CVListItem(text='Desk-wide ownership for Risk and '
                                'Profit/Loss(PL) reporting'),
                  md.CVListItem(text='Re-engineered QA infrastructure to '
                                'add first-level break analysis to automated '
                                'tests'),
                  md.CVListItem(text='Developed mathematical approximation '
                                'for regulatory risk requirement'), ]
    jpm_prd_mgmt = md.CVListHeading(text='Product Management',
                                    items=jpdm_items)

    jpjm_items = [md.CVListItem(text='Managed interface between '
                                'management\'s Waterfall and engineer\'s '
                                'Agile project management styles'),
                  md.CVListItem(text='Overhauled change controls and change '
                                'management for compatible with Agile and '
                                'Continuous Integration projects'),
                  md.CVListItem(text='Designed, developed, delivered, and '
                                'tested Front to Back PL and Risk reporting '
                                'python framework requiring computationally '
                                'correct, performant, and reusable reporting '
                                'modules written in a proprietary framework '
                                'called Athena, utilizing a customized '
                                'object oriented database'),
                  md.CVListItem(text='Determined minimum acceptable scope '
                                'by limiting feature creep and challenging '
                                'stakeholders in order to meet aggressive '
                                'deadlines'), ]
    jpm_prj_mgmt = md.CVListHeading(text='Project Management',
                                    items=jpjm_items)

    jcrm_items = [md.CVListItem(text='Encouraged team adoption of Agile '
                                'methodologies'),
                  md.CVListItem(text='Rebuilt team\'s reputation after an '
                                'implementation failure'),
                  md.CVListItem(text='Worked up management chain and across '
                                'business lines to develop critical '
                                'production capabilities'),
                  md.CVListItem(text='Assertive and confident when descoping, '
                                'deprioritizing'),
                  md.CVListItem(text='Achieved reputation for creatively '
                                'solving problems and dealing with difficult '
                                'personalities'), ]
    jpm_crm_mgmt = md.CVListHeading(text='Relationship Management',
                                    items=jcrm_items)

    jqal_items = [
        md.CVListItem(
            text='Motivated adoption of test driven design'),
        md.CVListItem(
            text='Improved pre-release tests which '
                 'decreased the number of false positives '
                 'and increased information content of failure '
                 'reports, enabling for faster error analysis'),
        md.CVListItem(
            text='Established test and release '
                 'procedures for new reporting module which '
                 'went live with zero defects in production')]

    jpm_qal_mgmt = md.CVListHeading(text='Quality Management',
                                    items=jqal_items)

    jpm_cvitemized = [jpm_rel_mgmt,
                      jpm_prd_mgmt,
                      jpm_prj_mgmt,
                      jpm_crm_mgmt,
                      jpm_qal_mgmt]

    jpm = md.CVEntry(start_yr=2010,
                     end_yr=2013,
                     title='Associate',
                     institution='JPMorgan',
                     city='New York City',
                     state='NY',
                     description='System Strategy and Implementation',
                     cvlistitems=jpm_cvlist_items,
                     cvitemized=jpm_cvitemized)

    mx_cvlist_items = [md.CVListItem(text='Managed a portfolio of software '
                                     'implementation projects'),
                       md.CVListItem(text='Represented software products '
                                     'internally and externally to educate '
                                     'users and promote sales')]

    mrm_items = [
        md.CVListItem(
            text='Migrated several client specific products '
            'to single master branch'), md.CVListItem(
            text='Approved final sign-off for client '
            'deliverables'), md.CVListItem(
            text='Rejected low quality developments and '
            'releases')]
    mx_rel_mgmt = md.CVListHeading(text='Release Management',
                                   items=mrm_items)

    mpdm_items = [md.CVListItem(text='Financing Product Manager(Americas)'),
                  md.CVListItem(text='Debt Market Product Specialist'),
                  md.CVListItem(text='Self directed research to gain edge in '
                                'product market'),
                  md.CVListItem(text='Specified system module re-engineering '
                                'to meet client and market practices'),
                  md.CVListItem(text='Demonstrated products to prospective '
                                'and existing clients'),
                  md.CVListItem(text='Pitched new modules and architecture '
                                'which improved testing work-flows, reduce '
                                'human costs, and improved client '
                                'satisfaction'), ]
    mx_prd_mgmt = md.CVListHeading(text='Product Management',
                                   items=mpdm_items)

    mpjm_items = [md.CVListItem(text='Lead for all Front office financing '
                                'products implementation for my client '
                                'portfolio, including UI/UX, Risk and PL '
                                'reporting, automatic trade booking, '
                                'and pre- and post-trade work-flows'),
                  md.CVListItem(text='Redesign and implement new testing '
                                'processes to remove test obstacles, decrease '
                                'testing time, and increase test coverage '
                                'and quality'),
                  md.CVListItem(text='Design and Implementation of UI/UX '
                                'modules on-site for clients')]
    mx_prj_mgmt = md.CVListHeading(text='Project Management',
                                   items=mpjm_items)

    mcrm_items = [
        md.CVListItem(text='Gained reputation for handling difficult '
                      'clients and turning around unhappy users'), md.CVListItem(
            text='Cooperated on multiple client and '
            'product teams'), md.CVListItem(
            text='Managed resource competition and client '
            'priorities'), md.CVListItem(
            text='Provided agency for client or Murex '
            'to optimize utilization of resources'), md.CVListItem(
            text='Resolve conflicts between product '
            'development and project deliverables'), md.CVListItem(
            text='Query end users and develop feedback '
            'process to enhance overall product'), md.CVListItem(
            text='Negotiated with end users to gain '
            'final approval for project deliverables'), ]
    mx_crm_mgmt = md.CVListHeading(text='Relationship Management',
                                   items=mcrm_items)

    mqal_items = [
        md.CVListItem(text='Write and automate tests for hard-to-automate '
                      'application functionality'),
        md.CVListItem(text='Advocate unit testing, which was against '
                      'philosophy at the time'),
        md.CVListItem(text='Decreased testing time across company by '
                      'standardizing processes')]

    mx_qal_mgmt = md.CVListHeading(text='Quality Management',
                                   items=mqal_items)

    mx_cvitemized = [mx_rel_mgmt,
                     mx_prd_mgmt,
                     mx_prj_mgmt,
                     mx_crm_mgmt,
                     mx_qal_mgmt]

    mx = md.CVEntry(start_yr=2007,
                    end_yr=2010,
                    title='Consultant',
                    institution='Murex',
                    city='New York City',
                    state='NY',
                    description='System Strategy and Implementation',
                    cvlistitems=mx_cvlist_items,
                    cvitemized=mx_cvitemized)

    edf_cvlist_items = [
        md.CVListItem(
            text='Built and maintained compute '
            'clusters for physics applications'),
        md.CVListItem(
            text='Designed, prototyped, and built '
            'waveform digitizer for particle '
            'detectors'),
        md.CVListItem(
            text='Designed and fabricated aluminum '
            'enclosures and face-plates using AutoCAD'),
        md.CVListItem(
            text='One of 4 full-time Engineers')]

    edf = md.CVEntry(start_yr=2003,
                     end_yr=2007,
                     title='Engineer',
                     institution='Boston University, Physics Dept.',
                     city='Boston',
                     state='MA',
                     description='Ran a portfolio of engineering projects of '
                     'varying scope and scale',
                     cvlistitems=edf_cvlist_items)

    experience = md.Section(title="Experience",
                            cventry=[acs_corp,
                                     jpm,
                                     mx,
                                     edf])
    sections.append(experience)

    mas_cv_cols = [
        md.CVColumns(
            items=[md.CVItems(text='Stochastic Models'),
                   md.CVItems(text='Analytics and Forecasts'), ]),
        md.CVColumns(
            items=[md.CVItems(text='Decision Theory'),
                   md.CVItems(text='Real Options'), ]),
        md.CVColumns(
            items=[md.CVItems(text='Operations Research'),
                   md.CVItems(text='Optimization'), ])
    ]

    mas = md.CVEntry(
        start_yr=2006,
        end_yr=2007,
        title='Master of Science: Financial Mathematics',
        institution='Boston University',
        city='Boston',
        state='MA',
        gpa='3.4',
        description='Study the tools and models of operational and investment '
        'decisions under uncertain conditions',
        cvcolumns=mas_cv_cols)

    ugr_cv_cols = [
        md.CVColumns(
            items=[md.CVItems(text='Very Large System Design'),
                   md.CVItems(text='Software Engineering'), ]),
        md.CVColumns(
            items=[md.CVItems(text='Control Systems'),
                   md.CVItems(text='Project Management'), ]),
    ]

    ugr = md.CVEntry(
        start_yr=2000,
        end_yr=2004,
        title='Bachelor of Science: Electrical Engineering',
        institution='Boston University',
        city='Boston',
        state='MA',
        gpa='3.2',
        honors='Cum Laude',
        description='Theory and application of electrical and electronic systems',
        cvcolumns=ugr_cv_cols)

    education = md.Section(title='Education',
                           cventry=[mas, ugr])
    sections.append(education)

    tech1_cv_cols = [
        md.CVColumns(
            name='Microsoft',
            items=[md.CVItems(text='Outlook'),
                   md.CVItems(text='Excel+VBA'),
                   md.CVItems(text='Project'),
                   md.CVItems(text='Visio'),
                   md.CVItems(text='Word'), ]),
        md.CVColumns(
            name='Linux',
            items=[md.CVItems(text='Debian, LFS'),
                   md.CVItems(text='LibreOffice'),
                   md.CVItems(text='LaTeX, Vim'), ]),
        md.CVColumns(
            name='Database',
            items=[md.CVItems(text='Postgresql'),
                   md.CVItems(text='Oracle'),
                   md.CVItems(text='SQLite'),
                   md.CVItems(text='MongoDB'),
                   md.CVItems(text='HDF5'), ]),
        md.CVColumns(
            name='CAD',
            items=[md.CVItems(text='OrCAD'),
                   md.CVItems(text='AutoCAD'),
                   md.CVItems(text='FreeCAD'), ]),
    ]

    tech2_cv_cols = [
        md.CVColumns(
            name='Programming',
            items=[md.CVItems(text='Python'),
                   md.CVItems(text='R'),
                   md.CVItems(text='C/C++/Java'), ]),
        md.CVColumns(
            name='Scripting',
            items=[md.CVItems(text='bash'),
                   md.CVItems(text='HTML, CSS, XML'),
                   md.CVItems(text='Javascript/JQuery'), ]),
        md.CVColumns(
            name='Source Control',
            items=[md.CVItems(text='git'),
                   md.CVItems(text='svn'), ]),
    ]

    pythn_cv_cols = [
        md.CVColumns(
            name='Python Packages',
            items=[md.CVItems(text='pyramid'),
                   md.CVItems(text='sqlalchemy'),
                   md.CVItems(text='chameleon'), ]),
        md.CVColumns(
            name=None,
            items=[md.CVItems(text='distutils'),
                   md.CVItems(text='nosetests'),
                   md.CVItems(text='coverage'), ]),
        md.CVColumns(
            name=None,
            items=[md.CVItems(text='pandas'),
                   md.CVItems(text='matplotlib'),
                   md.CVItems(text='numpy/scipy'),
                   md.CVItems(text='pytables'), ]),
        md.CVColumns(
            name=None,
            items=[md.CVItems(text='selenium'),
                   md.CVItems(text='subprocess'),
                   md.CVItems(text='multiprocess'), ]),
    ]
    tech_cols = [md.CVColumnGroup(cvcolumns=tech1_cv_cols)]
    tech_cols.append(md.CVColumnGroup(cvcolumns=tech2_cv_cols))
    tech_cols.append(md.CVColumnGroup(cvcolumns=pythn_cv_cols))

    tech = md.Section(title='Technology',
                      cvcolumngroups=tech_cols)
    sections.append(tech)

    pers_list = [
        md.CVListItem(
            text='Ask me about my website idea!'),
        md.CVListItem(
            text='I love to ride my bikes (plural, though '
            'not at the same time), whether it\'s banging '
            'around the city, up to Bear Mountain, or out to '
            'Montauk.  Cycling is very much my Zen garden.'), ]

    personal = md.Section(title='Personal',
                          cvlistitems=pers_list)

    sections.append(personal)

    resume = md.Resume(
        style='casual',
        color='red',
        title='Kickstarter\'s VP of Engineering',
        footnotestyle='symbols',
        sections=sections)

    me.resumes = [resume]

    with transaction.manager:
        db.add(me)
        db.flush()
        db.commit()
    return True

objectives = 'Observe and learn from those engaged with and dependent on ' \
    'Engineering to assess current processes, problems, concerns, and preferences. ' \
    'Work with individuals and teams to realize the most efficient and optimal ' \
    'approaches for the short, medium, and long term. Evangelize a culture of ' \
    'self evaluation and evolution with business and personnel needs. ' \
    'Implement proved methods to increase engineering output without sacrificing ' \
    'enjoyment. Offer structure or freedom to individuals to promote excellence ' \
    'and personal growth. Tailor project and product management tools to the ' \
    'culture and environment to allow for flexibility and for the best processes ' \
    'to emerge'

if __name__ == '__main__':
    run()
