from odoo import fields, models

class CompanyManagementPosSetting(models.Model):
    _name = "company.management.pos.setting"
    _description = "POS Setting"
    _rec_name = "name"

    name = fields.Char(string="Nama Titik penjualan (POS)", required=True)
    allow_credit_sales = fields.Boolean(string="Pilihan termin penjualan kredit yang diijinkan")
    allow_cash_sales = fields.Boolean(string="Pilihan termin penjualan cash yang diijinkan")
    default_cash_account_id = fields.Many2one("account.account", string="Akun cash default")
    location_id = fields.Many2one("stock.location", string="Lokasi Titik penjualan (POS)")
    active = fields.Boolean(default=True)
