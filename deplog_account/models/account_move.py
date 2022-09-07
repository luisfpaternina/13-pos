# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    def gt_save_associated(self):
        for rec in self.invoice_line_ids:
            if rec.partner_id:
                rec.write({'associated_id': rec.partner_id.id})






class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    associated_id = fields.Many2one(
        'res.partner',
        string="Associated")
