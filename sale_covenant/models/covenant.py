# coding: utf-8
# © 2017 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleCovenant(models.Model):
    _name = "sale.covenant"

    @api.model
    def _default_company(self):
        return self.env['res.company']._company_default_get()

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True,
        help="The active field allows you to make your record "
             "without effect but without remove it.")
    company_id = fields.Many2one(
        comodel_name='res.company', string='Company', index=1,
        default=_default_company)
    setting_rule_ids = fields.One2many(
        comodel_name='record.setting.rule', inverse_name='model_ref_id',
        string='Setting rules',
        help="")


class RecordSettingRule(models.Model):
    _inherit = "record.setting.rule"

    covenant_id = fields.Many2one(
        comodel_name='sale.covenant', string='Covenant')
