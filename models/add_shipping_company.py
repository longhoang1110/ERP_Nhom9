from odoo import api, fields, models


class AddSC(models.Model):
    _name = 'add.sc'

    code_Sc = fields.Char(string='Mã đơn vị vận chuyển', size=11, required=True)
    name_sc = fields.Char(string='Tên đơn vị vận chuyển', size=128, required=True)

    country_id = fields.Many2one('res.country', string='Quốc gia')
    transport = fields.Char(string='Phương tiện vận chuyển', required= True)
    city_id = fields.Many2one('add.city', string='City', required=True)
    diachict_id = fields.Char(string = 'Địa chỉ cụ thể', required = True)
