# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class CRMCustomerRequest(models.Model):
    _name = 'crm.customer.request'
    _description = 'Custommer Requests Management'
    _rec_name = "opportunity_id"
    
    product_id = fields.Many2one(
        comodel_name="product.template", 
        string="Product", 
        required=True)
    
    opportunity_id = fields.Many2one(
        comodel_name="crm.lead",
        required=True)
    
    date_request = fields.Date(
        "Request Date",
        default = fields.Date.today(),
        require=True,
        readonly=True)
    
    description = fields.Text(
        string="Description")
    
    qty = fields.Float(
        string="Quantity", 
        required=True)
    
