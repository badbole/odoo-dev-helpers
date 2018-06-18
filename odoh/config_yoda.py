
branch = '10.0'
root = "/media/data/code/ODOO_10"
sym_dest = "/media/data/code/ODOO_10/symlink"
symlink = {
    "_info_": 2,
    "_clean_": True, #default False, clean symlink dir from extras not listed

    "_only_": [
        'OCA',
        'dajmi5'
    ],
    "dajmi5": {
        "_only_": [
            "odoo-comunity-themes",
            "d5_scenario",
        ],
        "odoo-comunity-themes": {
            "_only_": ["backend_theme_v10"]
        }
    },
    "OCA": {
        "_only_": [
            'server-tools',
            'web',
            "knowledge",
            ],
        "server-tools": {
            "_only_": [
                "base_export_manager",
                "base_export_security",
                "base_suspend_security",
                "base_technical_features",
                "disable_odoo_online",
                "module_prototyper",
                "auditlog",
                "auth_admin_passkey",
                "auth_brute_force",
                "auth_session_timeout",
            ]
            },
        "web": {
            "_only_": [
                "help_online",
                "web_environment_ribbon",
                "web_no_bubble",
                "web_notify",
                "web_responsive",

            ]
        }
    },
}


