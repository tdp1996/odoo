# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Request'

    name = fields.Char('Purchase Reference', readonly=True, required=True, copy=False, default='New')

    department_id = fields.Many2one(
        comodel_name='hr.department',
        string="Department",
        default=lambda self: self.env.user.department_id.id,
        required=True)
    
    request_id = fields.Many2one(
        comodel_name='res.users', 
        string="Requested By", 
        default=lambda self: self.env.user,
        required=True)
    
    approver_id = fields.Many2one(
        comodel_name='res.users',
        string="Approver",
        required=True)

    date_request = fields.Date(
        string="Request Date",
        default=fields.Date.context_today,
        required=True)
    
    date_approve = fields.Date(
        string="Approve Date")
    
    description = fields.Text(string="Description")

    state = fields.Selection(
        selection=[
            ('draft', "Quotation"),
            ('wait', "Waiting"),
            ('approved', "Approved"),
            ('cancel', "Cancelled"),
        ],
        string="Status",
        default='draft')
    
    request_line_ids = fields.One2many(
        comodel_name='purchase.request.line',
        inverse_name='request_id',
        string='Request Line')

    total_qty = fields.Float(
        compute='_compute_total_quantity',
        string="Total Quantity")

    total_amount = fields.Float(
        compute='_compute_total_amount',
        string="Total Amount")

    @api.depends('request_line_ids.qty')
    def _compute_total_quantity(self):
        for record in self:
            record.total_qty = sum(line.qty for line in record.request_line_ids)

    @api.depends('request_line_ids.total')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = sum(line.total for line in record.request_line_ids)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.request')
            return super(PurchaseRequest, self).create(vals)
          
        
    # ACTIONS
    def action_pr_save(self):
        pass

    def action_pr_cancel(self):
        pass

    def action_request_approval(self):
        pass
    



