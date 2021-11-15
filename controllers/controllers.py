# -*- coding: utf-8 -*-
# from odoo import http


# class AcsHmsMrCommissionExtension(http.Controller):
#     @http.route('/acs_hms_mr_commission_extension/acs_hms_mr_commission_extension/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/acs_hms_mr_commission_extension/acs_hms_mr_commission_extension/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('acs_hms_mr_commission_extension.listing', {
#             'root': '/acs_hms_mr_commission_extension/acs_hms_mr_commission_extension',
#             'objects': http.request.env['acs_hms_mr_commission_extension.acs_hms_mr_commission_extension'].search([]),
#         })

#     @http.route('/acs_hms_mr_commission_extension/acs_hms_mr_commission_extension/objects/<model("acs_hms_mr_commission_extension.acs_hms_mr_commission_extension"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('acs_hms_mr_commission_extension.object', {
#             'object': obj
#         })
