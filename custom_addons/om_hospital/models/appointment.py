from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name ='hospital.appointment'
    _inherit=['mail.thread']
    _description = 'Hospital Appointment'
    _rec_name='patient_id'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    date_appointment = fields.Date(string="Date")
    note = fields.Text(string="Note")