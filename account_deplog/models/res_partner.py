# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    property_product_pricelist = fields.Many2one(
        'product.pricelist', 'Pricelist', compute=False, company_dependent=False,
        help="This pricelist will be used, instead of the default one, for sales to the current partner")
