# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'






class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    associated_id = fields.Many2one(
        'res.partner',
        string="Associated")

    def save_associated(self):
        for rec in self:
            if rec.partner_id:
                rec.write({'associated_id': rec.partner_id.id})
