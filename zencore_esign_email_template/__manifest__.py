# -*- coding: utf-8 -*-
{
    'name': 'ZenCore eSign Email Templates',
    'version': '18.0.1.0.0',
    'category': 'Sign',
    'summary': 'Custom, reusable email templates (header/body/footer) for eSign signature requests',
    'description': """
Adds a configurable "Email Templates" model for the Sign module.

- Configurations > Email Templates: manage reusable header/body/footer designs.
- sign.send.request wizard: pick a template (field placed right after Reminder).
- The selected template's header/body/footer are injected into Odoo's stock
  sign_template_mail_request QWeb template via inheritance. The default
  greeting, "Sign document" button, validity note, warning and terms are
  UNCHANGED - only extra header/body/footer blocks are added around them.
""",
    'depends': ['sign'],
    'data': [
        'security/ir.model.access.csv',
        'views/sign_email_template_views.xml',
        'views/sign_send_request_views.xml',
        'data/mail_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application': False,
}
