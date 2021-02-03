from odoo import models, fields, api

class SalesOrderCancel(models.Model):
    _inherit="sale.order"

    @api.multi
    def action_cancel(self):
        print "change function"
        super(SalesOrderCancel,self).action_cancel()
        