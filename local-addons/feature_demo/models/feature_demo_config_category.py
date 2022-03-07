from odoo import models, fields, api, _

class FeatureDemoConfigCategory(models.Model):
    _name = "feature.demo.config.category"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [('unique_name', 'UNIQUE(name)', 'Category name is exist!')]