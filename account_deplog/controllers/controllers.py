# -*- coding: utf-8 -*-
# from odoo import http


# class AccountDeplog(http.Controller):
#     @http.route('/account_deplog/account_deplog/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_deplog/account_deplog/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_deplog.listing', {
#             'root': '/account_deplog/account_deplog',
#             'objects': http.request.env['account_deplog.account_deplog'].search([]),
#         })

#     @http.route('/account_deplog/account_deplog/objects/<model("account_deplog.account_deplog"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_deplog.object', {
#             'object': obj
#         })
