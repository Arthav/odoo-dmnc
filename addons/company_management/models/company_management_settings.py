# addons/company_management/models/company_management_settings.py
from odoo import api, fields, models


class CompanyManagementSettings(models.Model):
    _name = "company.management.settings"
    _description = "Company Management Settings"
    _rec_name = "company_id"

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        default=lambda self: self.env.company,
        ondelete="cascade",
    )

    # --- Laporan Buku Besar (GL) ---
    fiscal_year_start = fields.Date(string="Fiscal Year Start")
    fiscal_year_end = fields.Date(string="Fiscal Year End")

    tax_period_months = fields.Integer(
        string="Tax Period (months)",
        default=1,
        help="Length of the tax period in months.",
    )
    tax_period_offset_months = fields.Integer(
        string="Tax Period End Offset (months)",
        default=1,
        help="How many months back the 'tax period end' is calculated.",
    )
    put_alternative_tax_include = fields.Boolean(
        string="Put alternative Tax Include on Docs",
    )
    suppress_tax_rates = fields.Boolean(
        string="Suppress Tax Rates on Docs",
    )

    # --- Harga Jual ---
    price_basis = fields.Selection(
        [
            ("before_tax", "Before Tax"),
            ("after_tax", "After Tax"),
        ],
        string="Basis for automatic price calculation",
        default="before_tax",
    )
    extra_price_percent = fields.Float(
        string="Extra Price from Standard Cost (%)",
        help="Extra percent added on top of standard cost.",
    )
    round_to_nearest = fields.Float(
        string="Round calculated prices to nearest",
        default=1.0,
        help="Example: 1 = round to whole currency; 100 = round to nearest hundred.",
    )

    # --- Optional Modules ---
    enable_manufacturing = fields.Boolean(string="Manufacturing")
    enable_fixed_assets = fields.Boolean(string="Fixed Assets")
    use_dimensions = fields.Boolean(string="Use Dimensions")

    # --- User Interface Options ---
    product_search_enabled = fields.Boolean(string="Search Product & Inventory")
    customer_search_enabled = fields.Boolean(string="Search Customer")
    supplier_search_enabled = fields.Boolean(string="Search Supplier")
    login_timeout_seconds = fields.Integer(
        string="Login Timeout (seconds)",
        default=1800,
    )

    _sql_constraints = [
        (
            "company_unique",
            "unique(company_id)",
            "There can only be one Management settings record per company.",
        )
    ]

    # Helpers so your other code can read settings easily
    @api.model
    def get_for_company(self, company=None):
        """Return the single settings record for a company (or False)."""
        company = company or self.env.company
        return self.search([("company_id", "=", company.id)], limit=1)

    @api.model
    def get_param(self, field_name, default=None, company=None):
        """Convenience accessor: settings.get_param('round_to_nearest')."""
        settings = self.get_for_company(company)
        if not settings:
            return default
        return getattr(settings, field_name, default)

    @api.model
    def action_open_settings(self):
        """Open the settings form for the current company, creating if needed."""
        company = self.env.company
        settings = self.search([('company_id', '=', company.id)], limit=1)
        if not settings:
            settings = self.create({'company_id': company.id})

        return {
            'type': 'ir.actions.act_window',
            'name': 'Company Settings',
            'res_model': 'company.management.settings',
            'view_mode': 'form',
            'res_id': settings.id,
            'target': 'current',
        }
