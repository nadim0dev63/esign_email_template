# -*- coding: utf-8 -*-
from odoo import fields, models


class SignRequest(models.Model):
    _inherit = 'sign.request'

    email_template_id = fields.Many2one(
        'sign.email.template',
        string='Email Template',
        help="Custom header/body/footer design used when the signature "
             "request email is sent. Leave empty to use the default look.")
