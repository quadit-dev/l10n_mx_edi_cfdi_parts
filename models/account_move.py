# -*- coding: utf-8 -*-
# Copyright 2022 - QUADIT, SA DE CV(https://www.quadit.mx)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models

class AccountInvoiceInherit(models.Model):
    _inherit = "account.move"

    def _concat_info(self, description, number):
        concat = description + " N DE SERIE " + number
        return concat