# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = 'project.task'

    sale_ids = fields.One2many('sale.order', 'task_id', string='Predidos de Venta')