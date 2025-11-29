from odoo import fields, models, api

class CompanyManagementGoodsTaxType(models.Model):
    _name = "company.management.goods.tax.type"
    _description = "Goods Tax Type"
    _rec_name = "name"

    name = fields.Char(string="Keterangan", required=True)
    is_fully_tax_exempt = fields.Selection(
        [('yes', 'Ya'), ('no', 'Tidak')],
        string="Bebas Pajak Penuh",
        default='no',
        required=True
    )
    is_default = fields.Selection(
        [('yes', 'Ya'), ('no', 'Tidak')],
        string="Default",
        default='no',
        required=True
    )
    line_ids = fields.One2many(
        "company.management.goods.tax.type.line",
        "goods_tax_type_id",
        string="Tax Lines"
    )

class CompanyManagementGoodsTaxTypeLine(models.Model):
    _name = "company.management.goods.tax.type.line"
    _description = "Goods Tax Type Line"

    goods_tax_type_id = fields.Many2one("company.management.goods.tax.type", string="Goods Tax Type")
    tax_item_id = fields.Many2one(
        "company.management.tax.item", 
        string="Nama Pajak", 
        required=True
    )
    tax_rate = fields.Float(
        related='tax_item_id.amount', 
        string="Rate",
        readonly=True
    )
    is_exempt = fields.Boolean(string="Bebas")

    _sql_constraints = [
        (
            "unique_tax_per_type",
            "unique(goods_tax_type_id, tax_item_id)",
            "A tax item can only appear once in a goods tax type.",
        )
    ]
