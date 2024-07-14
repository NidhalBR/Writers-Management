# -*- coding: utf-8 -*-
{
    'name': "lmw_writer_management",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['product', 'base','sale'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'report/report_template.xml',
        'report/writers_report.xml',
        'report/list_template.xml',
        'report/writers_list.xml',


        'views/product_view.xml',
        'views/speciality_view.xml',
        'views/institution_view.xml',
        'views/views.xml',
        'views/institution_view.xml',
        #'views/menuitems.xml',
        'views/templates.xml',



    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    "installable": True,
    "application": True,
    "license": "LGPL-3"
}

