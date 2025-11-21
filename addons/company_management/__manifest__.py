# addons/company_management/__manifest__.py
{
    "name": "Company Management Settings",
    "version": "1.0.0",
    "summary": "Extra company / GL / price and UI settings (FA-style screen).",
    "author": "Arth",
    "category": "Settings",
    "website": "",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/company_management_settings_views.xml",
    ],
    "installable": True,
    "application": False,
}
