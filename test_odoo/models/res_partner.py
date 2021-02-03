from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

#para modificar un campo se tiene que llamar igual
    notify_email=fields.Selection([('none',"None"),('always','Always'),('temp','Temp')])

    descripcion= fields.Char(string="Descripcion")
    valor =fields.Integer()