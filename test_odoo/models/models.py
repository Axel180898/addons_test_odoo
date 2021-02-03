# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError
from odoo.addons import decimal_precision as dp

class test_odoo(models.Model):
    _name = 'test_odoo.test_odoo'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    name = fields.Char()
    folio=fields.Char("Folio")
    value = fields.Integer()
    hireDate = fields.Date()
    active = fields.Boolean()
    salary = fields.Float(digits=dp.get_precision('test_precision'))
    status = fields.Selection([('draf', 'Draf'),('active','Active'),('inactive','Inactive')],default="active", required=True)
    selectorField=fields.Selection([('selected','Selected'),('unselected','Unselected')])
    partner_id = fields.Many2one('res.partner' ,string='Cliente')
    sale_ids = fields.Many2many('sale.order')
    TotalSales = fields.Integer(compute='countSales', store=True)
    details_id=fields.One2many('test_odoo.test_odoo.details','test_odoo_id', string='Detalles')
    # sale_id = fields.One2many('sale.order','partner_id')
    binary_field_image = fields.Binary()
    # binary_field_file = fields.Binary()

    #campos relacionales
    phone=fields.Char(related='partner_id.phone')

    @api.model
    def create(self, vals):
        vals['folio']=self.env['ir.sequence'].next_by_code("Test_odoo_codice_test")
        result =super(test_odoo,self).create(vals)
        return result
    @api.multi
    def test_pr(self):
        self.write({'name':"Antoine"})
    # @api.depends('sale_ids')
    @api.multi
    def countSales(self):
        for rec in self:
            if (len(rec.sale_ids)>0):
                suma=0
                for sale in rec.sale_ids:
                    suma=suma+1
                rec.TotalSales=suma
    @api.multi
    def NewTest(self):
        for rec in self:
            if rec.partner_id:
                sale_ids = self.env['sale.order'].search([('partner_id','=',rec.partner_id.id)])
                rec.value = len(sale_ids)
                for sale in sale_ids:
                    for line in sale.order_line:
                        print line.product_id.name
            else:
                raise UserError(_('Please Select client.'))
    @api.multi
    def cancel_Orders(self):
        for rec in self:
            if (len(rec.sale_ids)>0):
                for sale in rec.sale_ids:
                    sale.action_cancel()

class details (models.Model):
    _name='test_odoo.test_odoo.details'
    test_odoo_id=fields.Many2one(
        'test_odoo.test_odoo', String="Test_odoo_id")
    descripcion=fields.Char()
    version=fields.Integer()