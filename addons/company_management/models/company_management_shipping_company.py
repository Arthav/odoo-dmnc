from odoo import fields, models

class CompanyManagementShippingCompany(models.Model):
    _name = "company.management.shipping.company"
    _description = "Shipping Company"
    _rec_name = "name"

    name = fields.Char(string="Nama", required=True)
    contact = fields.Char(string="Kontak")
    phone = fields.Char(string="No Telepon")
    phone2 = fields.Char(string="Telepon 2")
    address = fields.Char(string="Alamat")
    active = fields.Boolean(default=True)
