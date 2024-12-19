from odoo import models, fields, api, _

class Lead(models.Model):
    _inherit = "crm.lead"

    request_ids = fields.One2many(
        "crm.customer.request",
        "opportunity_id",
        "Customer Request",
        readonly=True)
    
    total_qty = fields.Float(
        "Total Quantity",
        compute="_compute_total",
        readonly=True)

    expected_revenue = fields.Monetary(
        'Expected Revenue',
        compute="_compute_total",
        currency_field='currency_id',
        tracking=True)
    
    currency_id = fields.Many2one(
        'res.currency', 
        compute='_get_company_currency', 
        readonly=True, string='Currency')

    @api.depends('request_ids.qty','request_ids.product_id.list_price')
    def _compute_total(self):
        for lead in self:
            lead.total_qty = sum(request.qty for request in lead.request_ids)

            lead.expected_revenue = sum(
                rec.qty * rec.product_id.list_price for rec in lead.request_ids
            )

    @api.model
    def _get_company_currency(self):
        for partner in self:
            if partner.company_id:
                partner.currency_id = partner.sudo().company_id.currency_id
            else:
                partner.currency_id = self.env.company.currency_id
    
