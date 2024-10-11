# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloConversaciones(http.Controller):
#     @http.route('/modulo_conversaciones/modulo_conversaciones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_conversaciones/modulo_conversaciones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_conversaciones.listing', {
#             'root': '/modulo_conversaciones/modulo_conversaciones',
#             'objects': http.request.env['modulo_conversaciones.modulo_conversaciones'].search([]),
#         })

#     @http.route('/modulo_conversaciones/modulo_conversaciones/objects/<model("modulo_conversaciones.modulo_conversaciones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_conversaciones.object', {
#             'object': obj
#         })
