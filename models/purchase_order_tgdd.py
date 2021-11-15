

from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    delivery_status = fields.Selection(selection=[
            ('nothing', 'Chưa có đơn hàng'), ('to_receive', 'Đang đợi hàng'),
            ('partial', 'Đã nhận một phần hàng'), ('received', 'Đã nhận đầy đủ hàng'),
            ('processing', 'Đang xử lý đơn hàng')
    ], string='Tình trạng hàng', compute='_compute_delivery_status', store=True,
        readonly=True, copy=False, default='nothing')
    
    shipping_company_t = fields.Many2one('add.sc', string='Đơn vị vận chuyển', required=True)
    chinhanh = fields.Many2one('add.branch', string='Chi nhánh', required = True)
    thanhpho = fields.Many2one('res.country.state', string='Thành phố', required= True)
    quocgia = fields.Many2one('res.country', string= 'Quốc gia', required= True)
    requested_by = fields.Many2one('res.partner', default=lambda self: self.env.user.partner_id.id, required=True)
    reviewed_by = fields.Many2one('hr.employee')


    @api.depends('state', 'order_line.qty_received')
    def _compute_delivery_status(self):
        for rec in self:
            pickings = self.env['stock.picking'].search([
                ('purchase_id', '=', rec.id)])
            orderlines = rec.mapped('order_line')
            if not pickings and not orderlines.filtered(lambda x:x.product_id.type == 'service'):
                rec.delivery_status = 'nothing'
            elif all(o.qty_received == 0 for o in orderlines):
                rec.delivery_status = 'to_receive'
            elif orderlines.filtered(lambda x: x.qty_received < x.product_qty):
                rec.delivery_status = 'partial'
            elif all(o.qty_received == o.product_qty for o in orderlines):
                rec.delivery_status = 'received'
            elif any(p.state in ('waiting', 'confirmed') for p in pickings):
                rec.delivery_status = 'processing'




