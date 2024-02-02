from odoo import models, api, fields


class Employees(models.Model):

    _name = "employees.data"


    name = fields.Char(string='Name')
    org_name = fields.Many2one('organization.data',string='Organization')
    dep_ids = fields.Many2many('departments.data',string='Department')

    @api.onchange('org_name')
    def onchange_class_id(self):
        if self.org_name:
            subject_ids=self.env['departments.data'].search([])
            self.dep_ids = subject_ids.filtered(lambda item: self.org_name in item.org_name)
            print(subject_ids)