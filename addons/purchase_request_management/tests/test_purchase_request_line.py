from odoo.tests import tagged
from odoo.tests.common import TransactionCase

@tagged('post_install', '-at_install')
class TestPurchaseRequestLine(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(TestPurchaseRequestLine, cls).setUpClass()

        cls.department = cls.env['hr.department'].create({
            'name': 'IT',
        })
        cls.request_user = cls.env['res.users'].create({
            'name': 'Request User',
            'login': 'request_user'
        })

        cls.approver_user = cls.env['res.users'].create({
            'name': 'Approver User',
            'login': 'approver_user'
        })
        cls.product = cls.env['product.template'].create({
            'name': 'Test Product',
            'list_price': 100.0,
            'uom_id': cls.env.ref('uom.product_uom_unit').id
        })
        cls.request = cls.env['purchase.request'].create({
            'department_id': cls.department.id,
            'request_id': cls.request_user.id,
            'approver_id': cls.approver_user.id,
            'date_request': '2024-01-01',
            'state': 'draft',
        })

    def test_compute_total(self):
        line = self.env['purchase.request.line'].create({
            'request_id': self.request.id,
            'product_id': self.product.id,
            'uom_id': self.product.uom_id.id,
            'qty': 10.0
        })
        self.assertEqual(line.total, 1000.0, "Total must be 1000.0")



        