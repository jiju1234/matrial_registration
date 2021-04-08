from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError


class MaterialRegistration(models.Model):
    _name = 'material.registration'
    _description = 'Material Registration'

    name = fields.Char('Material Name',required=True)
    material_code = fields.Char(required=True)
    material_ype = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')],required=True,store=True)
    partner_id = fields.Many2one('res.partner','Supplier',required=True)
    material_buy_price = fields.Float('Material Buy Price',required=True)

    @api.constrains('material_buy_price')
    def _material_price_checking(self):
        for rec in self:
            if rec.material_buy_price:
                if rec.material_buy_price<100:
                    raise ValidationError(_('Material Buy Price Must be Greater than 100'))



