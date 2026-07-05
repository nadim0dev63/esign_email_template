# -*- coding: utf-8 -*-
from odoo import fields, models


class SignEmailTemplate(models.Model):
    _name = 'sign.email.template'
    _description = 'Sign Email Template'
    _order = 'name'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)

    # sanitize=True (default) on purpose: strips <script>/tracking-pixel style
    # markup that would otherwise hurt spam score, while still allowing
    # normal rich-text design (colors, images, links).
    header = fields.Html(
        string='Header',
        help="Shown above the default greeting. Keep it mostly text; "
             "a single logo image is fine, avoid large image-only blocks.")
    body = fields.Html(
        string='Body',
        help="Extra content shown above the 'Sign document' button, "
             "in addition to the per-request message.")
    footer = fields.Html(
        string='Footer',
        help="Shown after the standard warning notice, before Terms.")

    preview_note = fields.Char(
        default="The 'Sign document' button and the security warning are "
                "always added automatically by Odoo and cannot be edited here.",
        readonly=True)
