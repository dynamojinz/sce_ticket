# -*- coding: utf-8 -*-
{
    'name': "SCE Ticket",

    'summary': """
        SCE ticket helper
        Developed for Administration Department
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Zhang Li",
    'website': "http://www.sce-re.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/views.xml',
        'views/ticket_templates.xml',
        'views/ticket.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}