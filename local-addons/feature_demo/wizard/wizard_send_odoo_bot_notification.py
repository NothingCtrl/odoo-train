# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo import SUPERUSER_ID

class WizardSendOdooBotNotification(models.TransientModel):
    _name = "wizard.send.odoo.bot.notification"
    _description = "Wizard Send Odoo Bot Notification"

    user_id = fields.Many2one("res.users", string="User")
    subject = fields.Char(string="Subject", default="Subject/Topic")
    message = fields.Char(string="Message", default="Demo notification message")

    def send_message(self):
        for record in self:
            odoobot_id = self.env['ir.model.data'].xmlid_to_res_id("base.partner_root")
            channel = self.env['mail.channel'].sudo().search([("name", '=', 'OdooBot'),
                                                              ('channel_partner_ids', 'in', [record.user_id.partner_id.id])])
            if not channel:
                channel = self.env['mail.channel'].with_context(mail_create_nosubscribe=True).sudo().create({
                    'channel_partner_ids': [(4, record.user_id.partner_id.id), (4, odoobot_id)],
                    'public': 'private',
                    'channel_type': 'chat',
                    'email_send': False,
                    'name': 'OdooBot'
                })
            # note: system auto add some notification based on odoobot_state, set value to 'idle' to remove
            # addons.mail_bot.models.mail_bot.MailBot._get_answer
            channel.with_user(SUPERUSER_ID).message_post(subject=record.subject, body=record.message,
                                                         message_type='comment', subtype='mail.mt_comment')