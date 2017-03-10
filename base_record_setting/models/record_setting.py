# coding: utf-8
# © 2017 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class RecordSettingRule(models.Model):
    _name = "record.setting.rule"

    @api.model
    def _default_company(self):
        return self.env['res.company']._company_default_get()

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True,
        help="The active field allows you to make your record "
             "without effect but without remove it.")
    type = fields.Selection(selection=[
        ('default', 'Default'), ('mandatory', 'Mandatory')],
        default='default')
    company_id = fields.Many2one(
        comodel_name='res.company', string='Company', index=1,
        default=_default_company)
    model_ref_id = fields.Many2one(
        comodel_name='ir.model', string='Model Ref', required=True)
    field_ref_id = fields.Many2one(
        comodel_name='ir.model.fields', string='Field Ref', required=True)
    field_ref_value = fields.Char(string='Field Ref Value')
    # field_ref_human_value = fields.Char(string='Field Ref Value')
    # model_dest_id = fields.Many2one(
    #     comodel_name='ir.model', string='Model Dest.', required=True)
    # field_dest_id = fields.Many2one(
    #     comodel_name='ir.model.fields', string='Field Dest.', required=True)
    # field_dest_value = fields.Char(string='Field Dest Value')
    # field_dest_human_value = fields.Char(string='Field Dest Value')

    @api.onchange('model_dest_id')
    def _onchange_model_dest(self):
        self.field_dest_id, self.field_dest_value = False, False
        domain = {'field_dest_id': [('model_id', '=', self.model_dest_id.id)]}
        return {'domain': domain}

    @api.onchange('model_ref_id')
    def _onchange_model_ref(self):
        self.field_ref_id, self.field_ref_value = False, False
        domain = {'field_ref_id': [('model_id', '=', self.model_ref_id.id)]}
        return {'domain': domain}
