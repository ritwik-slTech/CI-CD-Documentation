from odoo import models, api, fields


class Subjects(models.Model):

    _name = 'subjects.data'

    name = fields.Char(string="Subject")
    class_ids = fields.Many2many('classes.data',string='Class')
    student_id = fields.Many2one('students.data',string='Student')