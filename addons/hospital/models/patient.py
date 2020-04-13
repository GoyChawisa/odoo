# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = "Hospital Patient"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    age_group = fields.Char(string="Age Group", compute='set_age_group', store=True)
    gender = fields.Selection(selection=[('Male','Male'),('Female','Female'),],string='Gender', default='Male', required=True)
    note = fields.Text()
    doctor_id = fields.Many2one('hospital.doctor', ondelete='set null', string="Docter", index=True)
    color = fields.Integer()

    @api.depends('age')
    def set_age_group(self):
        for r in self:
            if r.age > 20:
                r.age_group = 'major'
            else:
                r.age_group = 'minor'