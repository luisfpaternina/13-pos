# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'






class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    associated_id = fields.Many2one(
        'res.partner',
        string="Associated")
