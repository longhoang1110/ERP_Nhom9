from odoo import api, fields, models


class AddBranch(models.Model):
    _name = 'add.branch'

    code = fields.Char(string='Mã chi nhánh', size=11, required=True)
    name = fields.Char(string='Tên chi nhánh', size=128, required=True)

    country_id = fields.Many2one('res.country', string='Country')
    city_id = fields.Many2one('res.country.state', string='City', required=True, domain="[('country_id', '=?', country_id)]")
    diachi_id = fields.Char(string = 'Địa chỉ cụ thể', required = True)
