from odoo import fields, models

class CompanyManagementRole(models.Model):
    _name = "company.management.role"
    _description = "User Role"

    name = fields.Char(string="Nama Peran", required=True)
    description = fields.Char(string="Deskripsi Peran")
    active = fields.Boolean(string="Aktif", default=True)

    # --- Setup Perusahaan ---
    perm_group_setup_company = fields.Boolean(string="Setup Perusahaan")
    
    # --- Pengaturan Khusus ---
    perm_group_special_settings = fields.Boolean(string="Pengaturan Khusus")
    
    # --- Konfigurasi Penjualan ---
    perm_group_sales_config = fields.Boolean(string="Konfigurasi Penjualan")
    
    # --- Transaksi Penjualan ---
    perm_group_sales_trans = fields.Boolean(string="Transaksi Penjualan")
    
    # --- Laporan terkait penjualan ---
    perm_group_sales_reports = fields.Boolean(string="Laporan terkait penjualan")
    
    # --- Konfigurasi Pembelian ---
    perm_group_purchase_config = fields.Boolean(string="Konfigurasi Pembelian")
    perm_purchase_price_change = fields.Boolean(string="Perubahan harga beli")
    
    # --- Transaksi Pembelian ---
    perm_group_purchase_trans = fields.Boolean(string="Transaksi Pembelian")
    perm_view_supplier_trans = fields.Boolean(string="Menampilkan transaksi Supplier")
    perm_change_supplier = fields.Boolean(string="Perubahan Supplier")
    perm_input_purchase = fields.Boolean(string="Input Pembelian")

    # --- Analisis Pembelian ---
    perm_group_purchase_analysis = fields.Boolean(string="Analisis Pembelian")

    # --- Konfigurasi Inventaris ---
    perm_group_inventory_config = fields.Boolean(string="Konfigurasi Inventaris")

    # --- Kegiatan Inventaris ---
    perm_group_inventory_activity = fields.Boolean(string="Kegiatan Inventaris")

    # --- Analisis Inventaris ---
    perm_group_inventory_analysis = fields.Boolean(string="Analisis Inventaris")

    # --- Konfigurasi Bank dan Akun GL ---
    perm_group_bank_gl_config = fields.Boolean(string="Konfigurasi Bank dan Akun GL")

    # --- Transaksi Bank dan Akun GL ---
    perm_group_bank_gl_trans = fields.Boolean(string="Transaksi Bank dan Akun GL")

    # --- Analisis Bank dan Akun GL ---
    perm_group_bank_gl_analysis = fields.Boolean(string="Analisis Bank dan Akun GL")

    # --- Dashboard ---
    perm_group_dashboard = fields.Boolean(string="Dashboard")
