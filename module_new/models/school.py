from odoo import models, api, fields


class School(models.Model):

    _name = "school.data"

    class_id = fields.Many2one('classes.data',string='Class')
    teachers_ids = fields.Many2many('teachers.data',string='Teachers')
    students_ids = fields.Many2many('students.data',string='Students')
    subjects_ids = fields.Many2many('subjects.data',string='Subjects')


    @api.onchange('class_id')
    def onchange_class_id(self):
        if self.class_id:
            subject_ids =self.env['subjects.data'].search([])
            sub_class_ids = subject_ids.filtered(lambda obj : self.class_id.id in obj.class_ids.ids)
            self.subjects_ids= [(6, 0, sub_class_ids.ids)]

            
            teacher_ids =self.env['teachers.data'].search([])
            sub_teachers = teacher_ids.filtered(lambda obj : self.class_id.id in obj.class_ids.ids)
            self.teachers_ids= [(6, 0, sub_teachers.ids)]

            students_ids =self.env['students.data'].search([('class_id','=',self.class_id.id)])
            self.students_ids= [(6, 0, students_ids.ids)]
