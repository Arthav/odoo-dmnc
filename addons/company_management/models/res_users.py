from odoo import fields, models

class ResUsers(models.Model):
    _inherit = "res.users"

    company_role_id = fields.Many2one(
        "company.management.role", 
        string="Level Akses"
    )
