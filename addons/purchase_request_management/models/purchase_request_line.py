from odoo import models, fields, api

class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'
    _description = 'Purchase Request Line'

    request_id = fields.Many2one(
        comodel_name='purchase.request',
        string="Requester",
        required=True,
        readonly=True)
    
    product_id = fields.Many2one(
        comodel_name='product.template',
        string="Product",
        required=True,
        readonly=True)
    
    uom_id = fields.Many2one(
        comodel_name='uom.uom',
        string="Unit Of Measure",
        required=True,
        readonly=True)
    
    qty = fields.Float(
        string="Quantity",
        required=True)
    
    qty_approve = fields.Float(
        string="Aprroved Quantity")
    
    total = fields.Float(
        compute='_compute_total',
        string='Total')
    
    @api.depends('qty','product_id.list_price')
    def _compute_total(self):
        for record in self:
            record.total = record.qty * record.product_id.list_price
    

    
