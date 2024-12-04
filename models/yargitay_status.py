# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class YargitayStatus(models.Model):
    _name = 'yargitay.status'
    _description = 'Yargıtay Durumları'
    _inherit = ['mail.thread']


    name = fields.Char(string='Yargıtay Durumları')