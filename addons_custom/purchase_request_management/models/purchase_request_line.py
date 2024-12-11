from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'
    _description = 'Purchase Request Line'

    request_id = fields.Many2one(
        comodel_name='purchase.request',
        string="Order Reference")
    
    state = fields.Selection(
        related='request_id.state',
        string="State",
        readonly=True)
    
    product_id = fields.Many2one(
        comodel_name='product.template',
        string="Product",
        required=True)
    
    uom_id = fields.Many2one(
        comodel_name='uom.uom',
        string="Unit Of Measure",
        required=True)
    
    price_unit = fields.Float(
        string="Unit Price",
        required=True
    )
    
    qty = fields.Float(
        string="Quantity",
        required=True)
    
    qty_approve = fields.Float(
        string="Aprroved Quantity")
    
    total = fields.Float(
        compute='_compute_total',
        string='Total',
        readonly=True)
    
    @api.model
    def unlink(self):
        for line in self:
            if line.request_id.state != 'draft':
                raise UserError("You are not allowed to delete purchase request details in a state other than 'draft'.")    
        return super(PurchaseRequestLine, self).unlink()
    
    @api.model
    def create(self, vals):
        purchase_request = self.env['purchase.request'].browse(vals.get('request_id'))
        if purchase_request.state != 'draft':
            raise UserError("You are only allowed to create purchase request details in a state other than 'draft'.")
        return super(PurchaseRequestLine, self).create(vals)
    
    @api.depends('qty','product_id.list_price', 'price_unit')
    def _compute_total(self):
        for record in self:
            record.total = 0.00
            if not record.price_unit:
                record.total = record.qty * record.product_id.list_price
            else:
                record.total = record.qty * record.price_unit
                
    @api.onchange('product_id')
    def _onchange_product_id(self):
        for record in self:
            if record.product_id:
                purchase_line = self.env['purchase.request.line'].search([
                    ('product_id', '=', record.product_id.id)
                ], order='create_date desc', limit=1)
                # record.price_unit = purchase_line.price_unit 
                record.uom_id = purchase_line.uom_id
    
    @api.onchange('qty_approve', 'price_unit')
    def _onchange_qty_approve_and_price(self):
        for record in self:
            if record.qty_approve and record.price_unit:
                record.total = record.qty_approve * record.price_unit
            else:
                record.total = record.qty_approve * record.product_id.list_price
    


