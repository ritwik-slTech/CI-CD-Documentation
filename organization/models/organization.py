from odoo import models, api, fields


class Organization(models.Model):

    _name = "organization.data"


    name = fields.Char(string='Name')
    dep_ids = fields.One2many('departments.data','org_name',string='Departments')
    emp_ids = fields.One2many('employees.data','org_name',string='Employees')