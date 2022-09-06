# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def post(self):
        rec = super(AccountMove, self).post()
        wrong_lines = move.is_invoice() and move.line_ids.filtered(lambda aml: aml.partner_id != move.commercial_partner_id and not aml.display_type)
        if wrong_lines:
            wrong_lines.partner_id = move.commercial_partner_id.id
        return rec 
