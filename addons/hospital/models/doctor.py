# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = "Hospital Doctor"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    gender = fields.Selection(selection=[('Male','Male'),('Female','Female'),],string='Gender', default='Male', required=True)
    patient_ids = fields.One2many('hospital.patient', 'doctor_id', string="Patient")
    user_ref = fields.Many2one('res.users', ondelete='set null', string="User ref",index=True,required=True)
