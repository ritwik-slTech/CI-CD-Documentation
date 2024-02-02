from odoo import models, api, fields


class Students(models.Model):

    _name = 'students.data'

    name = fields.Char(string="Student Name")
    class_id = fields.Many2one('classes.data',string="Class Name")
    # schoolName = fields.Many2one('classes.data',string="schoolName")
    class_teacher_ids = fields.Many2many('teachers.data',string="Class Teacher")
    subject_ids = fields.One2many('subjects.data','student_id',string='Subject')

    # @api.onchange('class_id')
    # def onchange_class_id(self):
    #     if self.class_id:
    #         subject_ids =self.env['subjects.data'].search([])
    #         sub_class_ids = subject_ids.filtered(lambda obj : self.class_id.id in obj.class_ids.ids)
    #         print(sub_class_ids)