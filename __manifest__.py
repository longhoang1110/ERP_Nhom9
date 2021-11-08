# -*- coding: utf-8 -*-

{
    'name': "Package Condition on Purchase Order",
    'summary': """Package Condition on Purchase Order""",
    'description': "This module adds package condition  on purchase order",
    'author': "Thien Nguyuen Quoc",
    'company': "Da Nang University of Economic",
    'website': "facebook.com/mitmap.az",
    'category': 'Purchase',
    'version': '14.0.1.0.1',
    'depends': ['purchase', 'stock', 'purchase_stock'],
    'data': ['views/purchase_tgdd_order.xml',
             'report/purchase_tgdd_order_templates.xml',
             'views/create_location.xml'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    "application": True,
}