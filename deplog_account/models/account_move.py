# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    associated_id = fields.Many2one(
        'res.partner',
        string="Associated")
