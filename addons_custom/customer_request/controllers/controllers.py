# -*- coding: utf-8 -*-
# from odoo import http


# class CustomerRequest(http.Controller):
#     @http.route('/customer_request/customer_request', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_request/customer_request/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_request.listing', {
#             'root': '/customer_request/customer_request',
#             'objects': http.request.env['customer_request.customer_request'].search([]),
#         })

#     @http.route('/customer_request/customer_request/objects/<model("customer_request.customer_request"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_request.object', {
#             'object': obj
#         })
