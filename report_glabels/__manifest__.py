# -*- coding: utf-8 -*-
{
    'name': "odoo-stock-picking",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'external_dependencies': {'python': ['csv',], 'bin': ['glabels-3-batch']},

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/report_view.xml',
        #"wizard/report_test.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo_report.xml',
    ],
    'sequence' : 5
}
