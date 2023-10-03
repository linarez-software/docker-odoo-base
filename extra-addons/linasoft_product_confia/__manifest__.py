# Copyright (C) 2019 Open Source Integrators
# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "linasoft_product_confia",
    "summary": "Config the product view to make it more accessible to Confia users",
    "version": "16.0.1.0.0",
    "category": "Accounting Management",
    "website": "https://github.com/orgs/linarez-software",
    "author": "Pasv",
    "depends": ["product","brand","product_brand","product_harmonized_system_stock"],
    "data": [
        "views/product_views.xml",
        "security/ir.model.access.csv",
        # "views/confia_view.xml",

    ],
    "installable": True,
}
