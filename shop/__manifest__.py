# -*- coding: utf-8 -*-
{
    'name': "Shop",

    'summary': """Manage Shop""",

    'description': """
        The purpose of this module is manage of shop.
        This module consist of information about:
        1) Product - name, cost price, price and product weight
        2) Customers - name, discount, currency
        3) Buy - quantity of products, price per item, full price and full weight
        4) Check - information about product and buying
    """,

    'author': "KaterynaIvanova",
    'website': "http://www.kativ.com",

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
        'views/views.xml',
        'views/templates.xml',
        'views/shop.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}