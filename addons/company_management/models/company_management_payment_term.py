from odoo import fields, models, api

class CompanyManagementPaymentTerm(models.Model):
    _name = "company.management.payment.term"
    _description = "Payment Term"
    _rec_name = "name"

    name = fields.Char(string="Deskripsi", required=True)
    payment_type = fields.Selection(
        [
            ('prepayment', 'Prepayment'),
            ('cash', 'Tunai'),
            ('days', 'Setelah sekian hari'),
            ('next_month_date', 'Tanggal tertentu bulan berikutnya'),
        ],
        string="Jenis Pembayaran",
        required=True,
        default='days'
    )
    days = fields.Integer(string="Hari (atau hari ke- pada bulan berikutnya)", default=0)
    days_display = fields.Char(string="Jatuh tempo setelah/hari", compute="_compute_days_display")
    active = fields.Boolean(default=True)

    @api.depends('payment_type', 'days')
    def _compute_days_display(self):
        for record in self:
            if record.payment_type == 'days':
                record.days_display = f"{record.days} hari"
            elif record.payment_type == 'next_month_date':
                record.days_display = f"Hari ke-{record.days} bulan berikutnya"
            else:
                record.days_display = "T/A"

    @api.onchange('payment_type')
    def _onchange_payment_type(self):
        if self.payment_type in ['cash', 'prepayment']:
            self.days = 0
