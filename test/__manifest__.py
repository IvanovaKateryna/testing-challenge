# -*- coding: utf-8 -*-
{
    'name': "TEST",

    'summary': """Test course""",

    'description': """Module for test work""",

    'author': "Kateryna",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu_test.xml',
        'views/res_partner.xml',
        'views/test.xml',
        'views/templates.xml',
    ],

}