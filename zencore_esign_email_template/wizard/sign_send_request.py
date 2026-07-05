# -*- coding: utf-8 -*-
from odoo import fields, models


class SignSendRequest(models.TransientModel):
    _inherit = 'sign.send.request'

    # Placed right after reminder_enabled/reminder in the view.
    email_template_id = fields.Many2one(
        'sign.email.template',
        string='Email Template',
        help="Optional custom design for the signature request email.")

    def create_request(self):
        sign_request = super().create_request()
        if self.email_template_id:
            sign_request.email_template_id = self.email_template_id.id
        return sign_request
