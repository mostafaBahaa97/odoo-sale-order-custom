# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    driver_name = fields.Char(string="Driver")
    car_number = fields.Char(string="Car Number")