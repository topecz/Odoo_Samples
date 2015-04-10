# -*- coding: utf-8 -*-
{
    'name': "default_value_many2one",

    'summary': """
        Default value Many2one""",

    'description': """
        This module will add a Many2one field under Sales > Products or Purchase > Products.
	This field is a Many2one to all the currencies in the database and will automatically fill in the currency
	that is filled in on our custom method.
    """,

    'author': "Yenthe Van Ginneken",
    'website': "http://doo.yenthevg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}