from odoo import fields, models, api

class CompanyManagementFiscalYear(models.Model):
    _name = "company.management.fiscal.year"
    _description = "Fiscal Year"
    _rec_name = "name"
    _order = "start_date desc"

    name = fields.Char(string="Fiscal Year", compute="_compute_name", store=True)
    start_date = fields.Date(string="Awal Tahun Fiskal", required=True)
    end_date = fields.Date(string="Akhir Tahun Fiskal", required=True)
    is_closed = fields.Selection(
        [('yes', 'Ya'), ('no', 'Tidak')],
        string="Ditutup",
        default='no',
        required=True
    )
    active = fields.Boolean(default=True)

    @api.depends('start_date', 'end_date')
    def _compute_name(self):
        for record in self:
            if record.start_date and record.end_date:
                record.name = f"{record.start_date.year} - {record.end_date.year}"
            elif record.start_date:
                record.name = str(record.start_date.year)
            else:
                record.name = "New"
