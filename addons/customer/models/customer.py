# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Patient(models.Model):
    _inherit = 'crm.lead'

    line_id = fields.Char(string="Line ID")
    facebook = fields.Char(string="Facebook")
    google_map = fields.Char(string="Google Map")
    customer_type = fields.Selection(selection=[('Retail','Retail'),('Wholesales','Whole sales'),('Project','Project'),],string='Customer Type')