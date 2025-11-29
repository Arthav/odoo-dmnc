from odoo import fields, models

class CompanyManagementTaxItem(models.Model):
    _name = "company.management.tax.item"
    _description = "Tax Item"
    _rec_name = "name"

    name = fields.Char(string="Deskripsi", required=True)
    amount = fields.Float(string="Nilai Patokan (%)")
    sales_account_id = fields.Many2one(
        "account.account", 
        string="Akun GL Penjualan", 
        required=True,
        domain="[('deprecated', '=', False)]"
    )
    purchase_account_id = fields.Many2one(
        "account.account", 
        string="Akun GL Pembelian", 
        required=True,
        domain="[('deprecated', '=', False)]"
    )
    active = fields.Boolean(string="Active", default=True)
