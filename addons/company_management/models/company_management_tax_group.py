from odoo import fields, models, api

class CompanyManagementTaxGroup(models.Model):
    _name = "company.management.tax.group"
    _description = "Tax Group"
    _rec_name = "name"

    name = fields.Char(string="Keterangan", required=True)
    line_ids = fields.One2many(
        "company.management.tax.group.line",
        "group_id",
        string="Tax Lines"
    )

class CompanyManagementTaxGroupLine(models.Model):
    _name = "company.management.tax.group.line"
    _description = "Tax Group Line"

    group_id = fields.Many2one("company.management.tax.group", string="Tax Group")
    tax_item_id = fields.Many2one(
        "company.management.tax.item", 
        string="Pajak", 
        required=True
    )
    is_main_tax = fields.Boolean(string="Pajak")
    is_shipping_tax = fields.Boolean(string="Pajak Pengiriman")

    _sql_constraints = [
        (
            "unique_tax_per_group",
            "unique(group_id, tax_item_id)",
            "A tax item can only appear once in a group.",
        )
    ]
