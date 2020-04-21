# -*- coding: utf-8 -*-
from odoo import fields, models, api


class AppointmentWizard(models.TransientModel):
    _name = 'create.appointment'
    _description = "Hospital Appointment"

    def _default_patient_name(self):
        return self.env['hospital.patient'].browse(self._context.get('active_id'))

    patient = fields.Many2one('hospital.patient', required=True, ondelete='set null', string="Patient name", index=True, default=_default_patient_name, readonly=True)
    patient_code_name = fields.Char(string="Patient", compute='get_patient')
    doctor = fields.Many2one('hospital.doctor', required=True, ondelete='set null', string="Docter name", index=True)
    doctor_code_name = fields.Char(string="Doctor", compute='get_doctor')
    dateTime = fields.Datetime('Date time', required=True, readonly=False, index=True, default=lambda self:fields.datetime.now())

    @api.depends('patient')
    def get_patient(self):
        for r in self:
            r.patient_code_name = r.patient.patient_code + ' : ' + r.patient.name

    @api.depends('doctor')
    def get_doctor(self):
        for r in self:
            r.doctor_code_name = r.doctor.doctor_code + ' : ' + r.doctor.name

    @api.multi
    def create_appointment(self):
        vals = {
            'dateTime': self.dateTime,
            'doctor': self.doctor.id,
            'doctor_code_name': self.doctor_code_name,
            'patient': self.patient.id,
            'patient_code_name': self.patient_code_name
        }
        self.env['hospital.appointment'].create(vals)



    