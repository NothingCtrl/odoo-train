# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class FeatureDemoConfig(models.Model):
    _name = "feature.demo.config"
    _description = "Feature Demo Config"
    _inherit = ['mail.thread']

    name = fields.Char(string="Name", tracking=True)
    value = fields.Text(string="Value", tracking=True)
    priority = fields.Integer(string="Priority", default=10, tracking=True)
    active = fields.Boolean(default=True, string='Active', tracking=True)
    categ_id = fields.Many2one("feature.demo.config.category", string="Category")

    _sql_constraints = [('unique_name', 'UNIQUE(name)', "This name is exist!")]