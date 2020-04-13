# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Patient(models.Model):
    _name = 'hospital.patient'
    _inherit = 'mail.thread'
    _description = "Hospital Patient"

    name = fields.Char(string="Name", required=True, track_visibility='always')
    age = fields.Integer(string="Age", required=True, track_visibility='onchange')
    age_group = fields.Char(string="Age Group", compute='set_age_group', store=True, track_visibility='onchange')
    gender = fields.Selection(selection=[('Male','Male'),('Female','Female'),],string='Gender', default='Male', required=True, track_visibility='onchange')
    note = fields.Text(track_visibility='onchange')
    doctor_id = fields.Many2one('hospital.doctor', ondelete='set null', string="Docter", index=True, track_visibility='onchange')
    color = fields.Integer()

    @api.depends('age')
    def set_age_group(self):
        for r in self:
            if r.age > 20:
                r.age_group = 'major'
            else:
                r.age_group = 'minor'