# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def post(self):
        rec = super(AccountMove, self).post()
        for move in self.sorted(lambda m: (m.date, m.ref or '', m.id)):
            if move.auto_post and move.date > fields.Date.today():
                raise UserError(_("This move is configured to be auto-posted on {}".format(move.date.strftime(get_lang(self.env).date_format))))
            wrong_lines = move.is_invoice() and move.line_ids.filtered(lambda aml: aml.partner_id != move.commercial_partner_id and not aml.display_type)
            if wrong_lines:
                wrong_lines.partner_id = move.commercial_partner_id.id
