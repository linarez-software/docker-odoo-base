# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    vendors_ids= fields.Many2many(
        comodel_name="res.partner",
        compute= "_compute_vendors_ids",
        string="Vendors",
        )
    
    bom_components_ids = fields.Many2many(
        comodel_name="mrp.bom",
        compute="_compute_bom_components_ids",
        string="bill of materials"
        )

    price_list_items_ids= fields.One2many(
    comodel_name="product.pricelist.item",
    inverse_name="product_tmpl_id")

    stock_existences_rules_ids= fields.One2many(
    comodel_name="stock.warehouse.orderpoint",
    inverse_name="product_tmpl_id")

    stock_existences_ids= fields.One2many(
    comodel_name="stock.quant",
    inverse_name="product_tmpl_id",
    readonly=True)

    @api.depends("seller_ids")
    def _compute_vendors_ids(self):
        for rec in self:
            vendors_ids = set()
            for supplier_info in rec.seller_ids:
                vendors_ids |= {supplier_info.partner_id.id}
            rec.write({"vendors_ids":[
                fields.Command.set(list(vendors_ids)),
            ]})

    @api.depends()
    def _compute_bom_components_ids(self):
        for rec in self:
            boms =self.env["mrp.bom"].search(['|', ('product_tmpl_id', '=', rec.id), ('byproduct_ids.product_id.product_tmpl_id', '=', rec.id)])
            rec.write({"bom_components_ids":[
                fields.Command.set((boms.mapped("id")))
            ]})
            

class ConfiaPrices(models.Model):
    _name = "linasoft_product_confia.prices_class"

    main_class_id = fields.Many2one(comodel_name="product.template", string="Main Class")

    description = fields.Char(string="Description")
    price = fields.Char(string="Price")
