from odoo import fields, models

class CompanyManagementTransactionReference(models.Model):
    _name = "company.management.transaction.reference"
    _description = "Transaction Reference"
    _rec_name = "name"

    name = fields.Char(string="Transaction type", required=True)
    prefix = fields.Char(string="Prefix")
    pattern = fields.Char(string="Pattern", required=True)
    is_standard = fields.Boolean(string="Patokan")
    memo = fields.Char(string="Memo")
