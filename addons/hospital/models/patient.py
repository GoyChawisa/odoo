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
    patient_code = fields.Char(string="Patient code", copy=False, default='ptxxx')

    @api.depends('age')
    def set_age_group(self):
        for r in self:
            if r.age > 20:
                r.age_group = 'major'
            else:
                r.age_group = 'minor'

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('hospital.patient') or '/'
        vals['patient_code'] = seq
        return super(Patient, self).create(vals)

    @api.multi
    def create_appointment_wizard(self):
        return {
            'id': 'launch_appointment_wizard',
            'name': 'Create Appointment',
            'view_type': 'form',
            'view_mode': 'form',
            'src_model': 'hospital.patient',
            'res_model': 'create.appointment',
            'target': 'new',
            'type': 'ir.actions.act_window',
            'key2': 'client_action_multi'
        }