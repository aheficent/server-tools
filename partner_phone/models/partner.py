# -*- coding: utf-8 -*-
# © 2016 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import models
from openerp.addons.base_phone_fields.fields import Phone


class ResPartner(models.Model):
    _inherit = 'res.partner'

    phone = Phone()
