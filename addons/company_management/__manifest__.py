# addons/company_management/__manifest__.py
{
    "name": "DMNC Company Management Settings",
    "version": "1.0.0",
    "summary": "Extra company / GL / price and UI settings (FA-style screen).",
    "author": "BNFN",
    "category": "Settings",
    "website": "http://www.bnfn.my.id",
    "license": "LGPL-3",
    "depends": ["base", "account"],
    "data": [
        "security/ir.model.access.csv",
        "views/company_management_role_views.xml",
        "views/company_management_user_views.xml",
        "views/company_management_transaction_reference_views.xml",
        "views/company_management_tax_item_views.xml",
        "views/company_management_tax_group_views.xml",
        "views/company_management_goods_tax_type_views.xml",
        "views/company_management_settings_views.xml",
    ],
    "installable": True,
    "application": False,
}
