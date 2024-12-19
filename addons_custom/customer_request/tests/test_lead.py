from odoo.tests.common import TransactionCase, tagged
from odoo.exceptions import UserError

@tagged('-at_install', 'post_install')
class TestLead(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(TestLead, cls).setUpClass()

        cls.product_1 = cls.env['product.template'].create({
            'name': 'Test Product 1',
            'list_price': 100.0,
        })
        cls.product_2 = cls.env['product.template'].create({
            'name': 'Test Product 2',
            'list_price': 200.0,
        })

        cls.lead = cls.env['crm.lead'].create({
            'name': 'Test Opportunity',
            'type': 'opportunity',
        })


        cls.request_1 = cls.env['crm.customer.request'].create({
            'product_id': cls.product_1.id,
            'opportunity_id': cls.lead.id,
            'qty': 2.0,  
            'description': 'First customer request',
        })

        cls.request_2 = cls.env['crm.customer.request'].create({
            'product_id': cls.product_2.id,
            'opportunity_id': cls.lead.id,
            'qty': 1.0, 
            'description': 'Second customer request',
        })

    def test_compute_total(self):
        self.lead._compute_total()
        expected_total_qty = 2.0 + 1.0
        expected_revenue_test = (1.00 * 200.0) + (2.00 * 100.0)
        self.assertEqual(self.lead.total_qty, expected_total_qty)
        self.assertEqual(self.lead.expected_revenue, expected_revenue_test)

        
        