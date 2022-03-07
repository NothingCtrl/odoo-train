# -*- coding: utf-8 -*-
{
    'name': "Odoo Feature Demo",

    'summary': """
        Demo Odoo feature in actions""",

    'description': "",

    'author': "Thang Duong Bao",
    'website': "https://camratus.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'wizard/wizard_send_odoo_bot_notification.xml',
        'views/feature_demo_config_views.xml',
        'views/feature_demo_config_category_views.xml',
        'views/menu.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ]
}
