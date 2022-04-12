# -*- coding: utf-8 -*-
# Copyright 2022 - QUADIT, SA DE CV(https://www.quadit.mx)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': "Add Lots/Serial Numbers in CFDI",
    'version': '15.0.1.0.0',
    'summary': "Module for add lots in the invoice",
    'author': 'QUADIT',
    'website': "https://www.quadit.mx",
    'support': 'support@quadit.mx',
    'category': 'Hidden',
    'depends': [
        "account",
        "l10n_mx_edi"
    ],
    'data': [
        'views/add_lots_invoice.xml'
            ],
    'demo': [],
    'images': [],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
