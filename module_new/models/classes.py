from odoo import models, api, fields


class Classes(models.Model):

    _name = "classes.data"


    name = fields.Char(string='Class Name')
    student_ids = fields.One2many('students.data','class_id',String="Student Data")
    subjects = fields.Many2many('subjects.data',string='Subject')
