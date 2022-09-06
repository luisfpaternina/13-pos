# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    task_id = fields.Many2one('project.task', string='Tareas1')
    num_operation = fields.Char(string='Referencia1', compute='_compute_num_operation', store=True)

    @api.depends('task_id.x_studio_referencia_ido')
    def _compute_num_operation(self):
        for record in self:
            record.num_operation = record.task_id.x_studio_referencia_ido
    
    def update_task_id(self):
        for record in self:
            if record.x_studio_tareas:
                record.task_id = record.x_studio_tareas[0].id
    
    def update_all_task_id(self):
        sales = self.search([('x_studio_tareas','!=',False)])
        sales.update_task_id()
    
    @api.onchange('task_id')
    def _onchange_analytic_account_id(self):
        account_analytic = False
        if self.task_id:
            # task = self.env['project.task'].browse(vals.get('task_id'))
            account_analytic = self.env['account.analytic.account'].search([('name','=',self.task_id.x_studio_referencia_ido)], limit=1)
        if account_analytic:
            self.analytic_account_id = account_analytic.id
        else:
            self.analytic_account_id = False
    
    def action_confirm(self):
        for record in self:
            if not record.analytic_account_id:
                raise ValidationError('Falta cuenta analítica - IDO')
        return super(SaleOrder, self).action_confirm()