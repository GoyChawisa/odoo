from odoo import fields, models

class Contact(models.Model):
    _inherit = 'res.partner'

    patient = fields.Many2one('hospital.patient', string="Patient")