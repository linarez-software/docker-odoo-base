# -*- coding: utf-8 -*-

from odoo import models, fields, api


class confia_product_view(models.Model):
    _inherit = "product.template"

    tree_view_price = fields.One2many(
        comodel_name="linasoft_product_confia.prices_class", inverse_name="main_class_id", string="Confia tree view"
    )

    # tree_view_price_description = fields.Monetary()

    # tree_view_total_price = fields.

    # tree_view_price_taxes = fields.



class ConfiaPrices(models.Model):
    _name = "linasoft_product_confia.prices_class"

    main_class_id = fields.Many2one(comodel_name="product.template", string="Main Class")

    description = fields.Char(string="Description")
    price = fields.Char(string="Price")
