# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """
        Hospital""",

    'description': """
        Manage course, classes, teachers, students, ...
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/patient_view.xml",
        "views/doctor_view.xml",
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
}
