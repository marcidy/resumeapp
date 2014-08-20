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
    username = u'marcidy'

    address = md.Address(street_num='28',
                         street_name='Sickles',
                         street_type='Street',
                         apt_num='A16',
                         city='New York City',
                         state='NY',
                         zip=10040,
                         user_id=username)

    phone = md.Phone(type='mobile',
                     country=1,
                     area_code=508,
                     prefix=364,
                     line_number=7529,
                     user_id=username)

    me = md.Person(first_name='Matthew',
                   last_name='Arcidy',
                   email='marcidy@gmail.com',
                   linkedin='www.linkedin.com/in/marcidy',
                   address=address,
                   phone=[phone],
                   user_id=username)

    sections = []
    sections.append(md.Section(title='Objectives',
                               description=objectives,
                               user_id=username))

    acs_list_items = [
        md.CVListItem(
            text='Design operation and business '
            'process for a Top 4 consulting firm\'s '
            'crowdsourcing unit, including work-flows '
            'and analytics',
            user_id=username),
        md.CVListItem(
            text='Investigate and model statistical '
            'relationship between economic news events '
            'and volatility indices',
            user_id=username)]

    acs_corp = md.CVEntry(start_yr=2013,
                          title='Founder',
                          institution='Arcidy Computational Services',
                          city='New York City',
                          state='NY',
                          description='Provide consultation and innovation '
                          'services for any problems related to the function '
                          'and business of computation',
                          cvlistitems=acs_list_items,
                          user_id=username)

    jpm_cvlist_items = [md.CVListItem(text='Develop, implement, and support '
                                      'systems for risk, profit and loss, and '
                                      'cash flow projection calculations',
                                      user_id=username)]

    jrm_items = [md.CVListItem(text='Lead change control for business '
                               'critical infrastructure',
                               user_id=username),
                 md.CVListItem(text='Organized transition from quarterly '
                               'release cycle to Continuous Integration',
                               user_id=username),
                 md.CVListItem(text='Prioritized git branches and merges',
                               user_id=username)]
    jpm_rel_mgmt = md.CVListHeading(text='Release Management',
                                    items=jrm_items,
                                    user_id=username)

    jpdm_items = [md.CVListItem(text='Desk-wide ownership for Risk and '
                                'Profit/Loss(PL) reporting',
                                user_id=username),
                  md.CVListItem(text='Re-engineered QA infrastructure to '
                                'add first-level break analysis to automated '
                                'tests',
                                user_id=username),
                  md.CVListItem(text='Developed mathematical approximation '
                                'for regulatory risk requirement',
                                user_id=username), ]
    jpm_prd_mgmt = md.CVListHeading(text='Product Management',
                                    items=jpdm_items,
                                    user_id=username)

    jpjm_items = [md.CVListItem(text='Managed interface between '
                                'management\'s Waterfall and engineer\'s '
                                'Agile project management styles',
                                user_id=username),
                  md.CVListItem(text='Overhauled change controls and change '
                                'management for compatible with Agile and '
                                'Continuous Integration projects',
                                user_id=username),
                  md.CVListItem(text='Designed, developed, delivered, and '
                                'tested Front to Back PL and Risk reporting '
                                'python framework requiring computationally '
                                'correct, performant, and reusable reporting '
                                'modules written in a proprietary framework '
                                'called Athena, utilizing a customized '
                                'object oriented database',
                                user_id=username),
                  md.CVListItem(text='Determined minimum acceptable scope '
                                'by limiting feature creep and challenging '
                                'stakeholders in order to meet aggressive '
                                'deadlines',
                                user_id=username), ]
    jpm_prj_mgmt = md.CVListHeading(text='Project Management',
                                    items=jpjm_items,
                                    user_id=username)

    jcrm_items = [md.CVListItem(text='Encouraged team adoption of Agile '
                                'methodologies',
                                user_id=username),
                  md.CVListItem(text='Rebuilt team\'s reputation after an '
                                'implementation failure',
                                user_id=username),
                  md.CVListItem(text='Worked up management chain and across '
                                'business lines to develop critical '
                                'production capabilities',
                                user_id=username),
                  md.CVListItem(text='Assertive and confident when descoping, '
                                'deprioritizing',
                                user_id=username),
                  md.CVListItem(text='Achieved reputation for creatively '
                                'solving problems and dealing with difficult '
                                'personalities',
                                user_id=username), ]
    jpm_crm_mgmt = md.CVListHeading(text='Relationship Management',
                                    items=jcrm_items,
                                    user_id=username)

    jqal_items = [
        md.CVListItem(
            text='Motivated adoption of test driven design',
            user_id=username),
        md.CVListItem(
            text='Improved pre-release tests which '
                 'decreased the number of false positives '
                 'and increased information content of failure '
                 'reports, enabling for faster error analysis',
            user_id=username),
        md.CVListItem(
            text='Established test and release '
                 'procedures for new reporting module which '
                 'went live with zero defects in production',
            user_id=username)]

    jpm_qal_mgmt = md.CVListHeading(text='Quality Management',
                                    items=jqal_items,
                                    user_id=username)

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
                     cvitemized=jpm_cvitemized,
                     user_id=username)

    mx_cvlist_items = [md.CVListItem(text='Managed a portfolio of software '
                                     'implementation projects',
                                     user_id=username),
                       md.CVListItem(text='Represented software products '
                                     'internally and externally to educate '
                                     'users and promote sales',
                                     user_id=username)]

    mrm_items = [
        md.CVListItem(
            text='Migrated several client specific products '
            'to single master branch', user_id=username), md.CVListItem(
            text='Approved final sign-off for client '
            'deliverables', user_id=username), md.CVListItem(
            text='Rejected low quality developments and '
            'releases', user_id=username)]
    mx_rel_mgmt = md.CVListHeading(text='Release Management',
                                   items=mrm_items)

    mpdm_items = [md.CVListItem(text='Financing Product Manager(Americas)', user_id=username),
                  md.CVListItem(text='Debt Market Product Specialist', user_id=username),
                  md.CVListItem(text='Self directed research to gain edge in '
                                'product market', user_id=username),
                  md.CVListItem(text='Specified system module re-engineering '
                                'to meet client and market practices', user_id=username),
                  md.CVListItem(text='Demonstrated products to prospective '
                                'and existing clients', user_id=username),
                  md.CVListItem(text='Pitched new modules and architecture '
                                'which improved testing work-flows, reduce '
                                'human costs, and improved client '
                                'satisfaction', user_id=username), ]
    mx_prd_mgmt = md.CVListHeading(text='Product Management',
                                   items=mpdm_items)

    mpjm_items = [md.CVListItem(text='Lead for all Front office financing '
                                'products implementation for my client '
                                'portfolio, including UI/UX, Risk and PL '
                                'reporting, automatic trade booking, '
                                'and pre- and post-trade work-flows', user_id=username),
                  md.CVListItem(text='Redesign and implement new testing '
                                'processes to remove test obstacles, decrease '
                                'testing time, and increase test coverage '
                                'and quality', user_id=username),
                  md.CVListItem(text='Design and Implementation of UI/UX '
                                'modules on-site for clients', user_id=username)]
    mx_prj_mgmt = md.CVListHeading(text='Project Management',
                                   items=mpjm_items)

    mcrm_items = [
        md.CVListItem(text='Gained reputation for handling difficult '
                      'clients and turning around unhappy users', user_id=username), md.CVListItem(
            text='Cooperated on multiple client and '
            'product teams', user_id=username), md.CVListItem(
            text='Managed resource competition and client '
            'priorities', user_id=username), md.CVListItem(
            text='Provided agency for client or Murex '
            'to optimize utilization of resources', user_id=username), md.CVListItem(
            text='Resolve conflicts between product '
            'development and project deliverables', user_id=username), md.CVListItem(
            text='Query end users and develop feedback '
            'process to enhance overall product', user_id=username), md.CVListItem(
            text='Negotiated with end users to gain '
            'final approval for project deliverables', user_id=username), ]
    mx_crm_mgmt = md.CVListHeading(text='Relationship Management',
                                   items=mcrm_items)

    mqal_items = [
        md.CVListItem(text='Write and automate tests for hard-to-automate '
                      'application functionality', user_id=username),
        md.CVListItem(text='Advocate unit testing, which was against '
                      'philosophy at the time', user_id=username),
        md.CVListItem(text='Decreased testing time across company by '
                      'standardizing processes', user_id=username)]

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
                    cvitemized=mx_cvitemized,
                    user_id=username)

    edf_cvlist_items = [
        md.CVListItem(
            text='Built and maintained compute '
            'clusters for physics applications', user_id=username),
        md.CVListItem(
            text='Designed, prototyped, and built '
            'waveform digitizer for particle '
            'detectors', user_id=username),
        md.CVListItem(
            text='Designed and fabricated aluminum '
            'enclosures and face-plates using AutoCAD', user_id=username),
        md.CVListItem(
            text='One of 4 full-time Engineers', user_id=username)]

    edf = md.CVEntry(start_yr=2003,
                     end_yr=2007,
                     title='Engineer',
                     institution='Boston University, Physics Dept.',
                     city='Boston',
                     state='MA',
                     description='Ran a portfolio of engineering projects of '
                     'varying scope and scale',
                     cvlistitems=edf_cvlist_items,
                     user_id=username)

    experience = md.Section(title="Experience",
                            cventry=[acs_corp,
                                     jpm,
                                     mx,
                                     edf],
                            user_id=username)
    sections.append(experience)

    mas_cv_cols = [
        md.CVColumns(
            items=[md.CVItems(text='Stochastic Models', user_id=username),
                   md.CVItems(text='Analytics and Forecasts', user_id=username), ]),
        md.CVColumns(
            items=[md.CVItems(text='Decision Theory', user_id=username),
                   md.CVItems(text='Real Options', user_id=username), ]),
        md.CVColumns(
            items=[md.CVItems(text='Operations Research', user_id=username),
                   md.CVItems(text='Optimization', user_id=username), ])
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
        cvcolumns=mas_cv_cols,
        user_id=username)

    ugr_cv_cols = [
        md.CVColumns(
            items=[md.CVItems(text='Very Large System Design', user_id=username),
                   md.CVItems(text='Software Engineering', user_id=username), ]),
        md.CVColumns(
            items=[md.CVItems(text='Control Systems', user_id=username),
                   md.CVItems(text='Project Management', user_id=username), ]),
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
        cvcolumns=ugr_cv_cols,
        user_id=username)

    education = md.Section(title='Education',
                           cventry=[mas, ugr],
                           user_id=username)
    sections.append(education)

    tech1_cv_cols = [
        md.CVColumns(
            name='Microsoft',
            items=[md.CVItems(text='Outlook', user_id=username),
                   md.CVItems(text='Excel+VBA', user_id=username),
                   md.CVItems(text='Project', user_id=username),
                   md.CVItems(text='Visio', user_id=username),
                   md.CVItems(text='Word', user_id=username), ],
            user_id=username),
        md.CVColumns(
            name='Linux',
            items=[md.CVItems(text='Debian, LFS', user_id=username),
                   md.CVItems(text='LibreOffice', user_id=username),
                   md.CVItems(text='LaTeX, Vim', user_id=username), ],
            user_id=username),
        md.CVColumns(
            name='Database',
            items=[md.CVItems(text='Postgresql', user_id=username),
                   md.CVItems(text='Oracle', user_id=username),
                   md.CVItems(text='SQLite', user_id=username),
                   md.CVItems(text='MongoDB', user_id=username),
                   md.CVItems(text='HDF5', user_id=username), ],
            user_id=username),
        md.CVColumns(
            name='CAD',
            items=[md.CVItems(text='OrCAD', user_id=username),
                   md.CVItems(text='AutoCAD', user_id=username),
                   md.CVItems(text='FreeCAD', user_id=username), ],
            user_id=username),
    ]

    tech2_cv_cols = [
        md.CVColumns(
            name='Programming',
            items=[md.CVItems(text='Python', user_id=username),
                   md.CVItems(text='R', user_id=username),
                   md.CVItems(text='C/C++/Java', user_id=username), ],
            user_id=username),
        md.CVColumns(
            name='Scripting',
            items=[md.CVItems(text='bash', user_id=username),
                   md.CVItems(text='HTML, CSS, XML', user_id=username),
                   md.CVItems(text='Javascript/JQuery', user_id=username), ],
            user_id=username),
        md.CVColumns(
            name='Source Control',
            items=[md.CVItems(text='git', user_id=username),
                   md.CVItems(text='svn', user_id=username), ],
            user_id=username),
    ]

    pythn_cv_cols = [
        md.CVColumns(
            name='Python Packages',
            items=[md.CVItems(text='pyramid', user_id=username),
                   md.CVItems(text='sqlalchemy', user_id=username),
                   md.CVItems(text='chameleon', user_id=username), ],
            user_id=username),
        md.CVColumns(
            name=None,
            items=[md.CVItems(text='distutils', user_id=username),
                   md.CVItems(text='nosetests', user_id=username),
                   md.CVItems(text='coverage', user_id=username), ],
            user_id=username),
        md.CVColumns(
            name=None,
            items=[md.CVItems(text='pandas', user_id=username),
                   md.CVItems(text='matplotlib', user_id=username),
                   md.CVItems(text='numpy/scipy', user_id=username),
                   md.CVItems(text='pytables', user_id=username), ],
            user_id=username),
        md.CVColumns(
            name=None,
            items=[md.CVItems(text='selenium', user_id=username),
                   md.CVItems(text='subprocess', user_id=username),
                   md.CVItems(text='multiprocess', user_id=username), ],
            user_id=username),
    ]
    tech_cols = [md.CVColumnGroup(cvcolumns=tech1_cv_cols, user_id=username)]
    tech_cols.append(md.CVColumnGroup(cvcolumns=tech2_cv_cols, user_id=username))
    tech_cols.append(md.CVColumnGroup(cvcolumns=pythn_cv_cols, user_id=username))

    tech = md.Section(title='Technology',
                      cvcolumngroups=tech_cols,
                      user_id=username)
    sections.append(tech)

    pers_list = [
        md.CVListItem(
            text='Ask me about my website idea!', user_id=username),
        md.CVListItem(
            text='I love to ride my bikes (plural, though '
            'not at the same time), whether it\'s banging '
            'around the city, up to Bear Mountain, or out to '
            'Montauk.  Cycling is very much my Zen garden.', user_id=username), ]

    personal = md.Section(title='Personal',
                          cvlistitems=pers_list,
                          user_id=username)

    sections.append(personal)

    resume = md.Resume(
        style='casual',
        color='red',
        title='Kickstarter\'s VP of Engineering',
        footnotestyle='symbols',
        sections=sections,
        user_id=username)

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
