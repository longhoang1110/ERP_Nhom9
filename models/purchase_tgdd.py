from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class tgdd(models.Model):
    _name = "purchase.tgdd"
    _inherit = 'purchase.order'  #
    _description = "extend Purchase model"

    # add new field

    deposit = fields.Integer("Số tiền đặt cọc")
    note = fields.Char("Ghi chú")

    # avoid error: Many2many fields purchase.tgdd.transaction_ids and purchase.order.transaction_ids use the same table and columns
    transaction_ids = fields.Many2many('purchase.order.transaction', 'tgdd_transaction_rel', 'purchase_id', 'transaction_id',
                                       string='Tags')
    # Many2many fields purchase.tgdd.tag_ids and sale.order.tag_ids use the same table and columns
    tag_ids = fields.Many2many('purchase.order.tag', 'tgdd_tag_rel', 'purchase_id', 'tag_id', string='Tags')