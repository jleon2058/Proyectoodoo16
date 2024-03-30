# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class modulo__jc(models.Model):
#     _name = 'modulo__jc.modulo__jc'
#     _description = 'modulo__jc.modulo__jc'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields,api

class Clase_condicion_pago(models.Model):
    _name='condicionpago.jc'
    
    name=fields.Char("Condicion de Pago")
    codigo_condpago=fields.Char("Condicion de Pago")
