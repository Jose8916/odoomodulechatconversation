# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Conversaciones(models.Model):
    _name = 'modulo.conversaciones'
    _description = 'Conversaciones'

    #name = fields.Char(string='Name')
    #responder = fields.Char(string='Responder')
    numeroticket = fields.Char(string='Numero Ticket')

    estadoconversacion = fields.Char(string='Estado Conversacion')

    firstusergroup = fields.Char(string='First User Group')
    ticketgroup = fields.Char(string='Ticket Group')
    attentiongroup = fields.Char(string='Attention Group')

    asesorinicial = fields.Char(string='Aesor Inicial')
    asesorfinal = fields.Char(string='Asesor Final')
    supervisor = fields.Char(string='Supervisor')
    empresa = fields.Char(string='Empresa')
    fecha = fields.Char(string='Fecha')
    fechainicio = fields.Char(string='Fecha inicio')
    horainicio = fields.Char(string='Hora Inicio')
    fechahandoff = fields.Char(string='Fecha Hand Off')

    fechafin = fields.Char(string='Fecha Fin')
    horafin = fields.Char(string='Hora Fin')

    fechaprimeraconversacion = fields.Char(string='Fecha Primera Conversacion')
    fechaultimaconversacion = fields.Char(string='Fecha Ultima Conversacion')
    tiempoprimerarespuesta = fields.Char(string='Tiempo Primera Respuesta')

    def abrir_modal(self):
        return self.env['ir.actions.act_window']._for_xml_id("modulo_conversaciones.modal_conversacion_action")

        # return {'type':'ir.actions.act_window',
        #         'res_model': 'modal.conversacion.wizard',
        #         'view_mode':'form',
        #         'target':'new'}