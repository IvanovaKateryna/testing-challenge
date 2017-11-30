# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Product(models.Model):
    _name = 'shop.product'
    _description = 'Product'

    name = fields.Char(string="Product", required=True)
    cost_price = fields.Float('Cost Price', digits=(6, 1), help="Cost price in dollars", required=True)
    price = fields.Float(digits=(6, 1), help="Price in dollars", required=True)
    weight = fields.Float(digits=(6, 1), help="Weight in kg", required=True)


class Customer(models.Model):
    _name = 'shop.customer'
    _description = 'Customer'

    name = fields.Char(string="Customer", required=True)
    discount_id = fields.Many2one('shop.discount',
        ondelete='cascade', string="Discount", required=True)
    currency_id = fields.Many2one('shop.currency',
        ondelete='cascade', string="Currency", required=True)


class Currency(models.Model):
    _name = 'shop.currency'
    _description = 'Currency'

    name = fields.Char(string="Currency",readonly=True, required=True)


class Discount(models.Model):
    _name = 'shop.discount'

    name = fields.Char(string="Discount",readonly=True, required=True)
# class shop(models.Model):
#     _name = 'shop.shop'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100