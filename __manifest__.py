# -*- coding: utf-8 -*-
{
    'name': 'Priority Role',
    "license": "LGPL-3",
    'summary': """
        Priority Role for PNS
        """,
    'description': """
        Priority Role for PNS
    """,
    'author': "Rehan | Fahmi Roihanul Firdaus",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['mail', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/role_views.xml',
        'views/karyawan_views.xml',
        'views/menu_views.xml'
    ]
}