# -*- coding: utf-8 -*-

from openerp import models, fields, api


class MinimalModel(models.Model):
    _name = 'test.model'
    name = fields.Char(required=True)


class LessMinimalModel(models.Model):
    _name = 'test.model2'
    name = fields.Char(required=True)


class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

