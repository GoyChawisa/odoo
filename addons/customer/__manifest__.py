# -*- coding: utf-8 -*-
{
    'name': "Customer",

    'summary': """
        Customer test""",

    'description': """
        Manage customer test
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customer',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','crm'],

    # always loaded
    'data': [
        # "security/security.xml",
        # "wizards/appointment_wizard.xml",
        "security/ir.model.access.csv",
        "views/customer_menu_view.xml",
        "views/customer_view.xml",
        # "views/doctor_view.xml",
        # "views/appointment_view.xml",
        # "views/contact_view.xml",

    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
}
