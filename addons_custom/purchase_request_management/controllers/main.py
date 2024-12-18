from odoo import http
from odoo.http import request

class Main(http.Controller):
    @http.route('/purchase_request/json', type='http', auth='none')
    def courses_json(self):
        record = request.env['purchase.request'].sudo().search([])
        html_result = '<html><body><ul>'
        for course in record:
            html_result += "<li> %s </li>" % course.name
        html_result += '</ul></body></html>'
        return html_result