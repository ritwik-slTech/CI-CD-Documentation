from odoo import models, api, fields


class Departments(models.Model):

    _name = "departments.data"


    name = fields.Char(string='Name')
    org_name = fields.Many2one('organization.data',string='Organization')
    emp_ids = fields.Many2many('employees.data',string='Employees')

    @api.onchange('org_name')
    def onchange_class_id(self):
        if self.org_name:
            var_emp_ids=self.env['employees.data'].search([])
            filter_emp_ids = var_emp_ids.filtered(lambda item: self.org_name.id == item.org_name.id)

            self.emp_ids = [(6, 0, filter_emp_ids.ids)]