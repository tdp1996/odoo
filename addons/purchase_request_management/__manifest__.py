# -*- coding: utf-8 -*-
{
    'name': "Purchase Request Management",

    'summary': """
        Manage department purchasing requests 
    """,

    # 'description': """
    #     Long description of module's purpose
    # """,

    # 'author': "My Company",
    # 'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 
                'purchase',
                'hr',
                'product'
            ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
