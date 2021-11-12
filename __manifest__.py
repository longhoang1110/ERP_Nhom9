# -*- coding: utf-8 -*-

{
    'name': "Purchase Oder",
    'summary': """Module hỗ trợ tính năng đặt hàng cho Thế Giới Di Động""",
    'description': "Bổ sung một số tính năng hỗ trợ cho chức năng đặt hàng, được thiết kế bới nhóm 9 lớp 44k21.1",
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