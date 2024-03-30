# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloJc(http.Controller):
#     @http.route('/modulo__jc/modulo__jc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo__jc/modulo__jc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo__jc.listing', {
#             'root': '/modulo__jc/modulo__jc',
#             'objects': http.request.env['modulo__jc.modulo__jc'].search([]),
#         })

#     @http.route('/modulo__jc/modulo__jc/objects/<model("modulo__jc.modulo__jc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo__jc.object', {
#             'object': obj
#         })
