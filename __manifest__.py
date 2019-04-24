# -*- coding: utf-8 -*-
# Copyright 2019 <Quadit S.A. de C.V.> (https://www.quadit.mx)
# Copyright 2019 Leticia González Contreras
# Copyright 2019 Lázaro Rodríguez Triana
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "Add Lots/Serial Numbers in CFDI",
    'version': '12.0.1.0.0',
    'summary': "Module for add lots in the invoice",
    'author':  'Quadit, S.A. de C.V.',
    'website': "https://www.quadit.mx",
    'category': 'Hidden',
    'depends': [
        "account",
        "l10n_mx_edi",
        "account_invoice_production_lot"
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
