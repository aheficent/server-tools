# coding: utf-8
# © 2017 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale Covenant",
    "summary": "Drive behavior on sale according to commercial conditions",
    "version": "10.0.1.0.0",
    "category": "Sale",
    "website": "https://www.akretion.com",
    "author": "Akretion, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base_record_setting",
        "sale",
    ],
    "data": [
        "views/covenant_view.xml",
    ],
}
