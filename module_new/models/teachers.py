from odoo import models, api, fields


class Teacher(models.Model):
    _name = 'teachers.data'

    name = fields.Char(string='teachers name')
    class_ids = fields.Many2many('classes.data',string='Class')
    # school = fields.Char(string="schoolName")
    student_ids = fields.Many2many('students.data',string="Student")
    subjects = fields.Many2many('subjects.data',string='Subject')
