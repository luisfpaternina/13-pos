# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_data_report_invoice_e(self):
        self.ensure_one()
        sale = self.env['sale.order'].search([('name','=',self.invoice_origin)])
        company_currency = self.company_id.currency_id
        rate = 1
        if self.currency_id != company_currency:
            currency =self.currency_id
            rate = currency._convert(rate, company_currency,self.company_id,self.invoice_date)
        task = False
        if sale:
            task = sale.task_id
        doc_trans = ''
        if task:
            task = task[0]
            doc_trans = ', '.join([x.x_name for x in task.x_studio_field_KRtGp])
        data = {
                'customer': self.partner_id.name or '-',
                'nit': self.partner_id.vat or '-',
                'address': self.partner_id.street or '-',
                'phone': self.partner_id.phone or (sale and sale.partner_id.mobile) or '-',
                'contact': sale and sale.partner_id.name or '-',
                'pay': self.invoice_payment_term_id.name or '-',
                'doc_trans': doc_trans or '-',
                'mercancia': task and task.x_studio_comodity or '-',
                'pedido': self.ref or (sale and sale.client_order_ref) or '-',
                'origin': 10,
                'destino': 11,
                'date': self.invoice_date or '-',
                'eta': task and task.x_studio_eta or '-',
                'date_venc': self.invoice_date_due or '-',
                'incoterm': sale and sale.x_studio_field_MlBXO.code or '-',
                'tasa': round(rate, 3) or '-',
                'ido': (sale and sale.num_operation) or (task and task.x_studio_referecia_ido) or '-',
                }
        return data