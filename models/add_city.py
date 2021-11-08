from odoo import api, fields, models


class AddCity(models.Model):
    _name = 'add.city'

    code = fields.Char(string='Mã thành phố', size=4, required=True)
    name = fields.Char(string='Tên thành phố', size=100, required=True)
    country_id = fields.Many2one('res.country', string='Country', required=True)

