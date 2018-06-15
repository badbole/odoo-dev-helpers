"""
Only symlink based on config_brundo_10 clone/pull config
"""
root = "/media/data/code/ODOO_10"
sym_dest = "/media/data/code/ODOO_10/symlink"
symlink = {
    "_info_": 2,
    "_clean_": True, #default False, clean symlink dir from extras not listed

    "_only_": [
        "uvid",
        "dajmi5",
        "OCA",
        "it-projects-llc",
    ],
    "dajmi5": {
        "_only_": [
            "odoo-comunity-themes",
            "odoo-test-data",

        ],
        "odoo-comunity-themes": {
            "_only_": ["backend_theme_v10"]
        }
    },

    "OCA": {
        "_only_": [
            'server-tools',
            'partner-contact',
            'web'
        ],
        "server-tools": {
            "_only_": [
                "base_export_security",
                "base_suspend_security",
                "base_technical_features",
                "disable_odoo_online",
                "module_prototyper",
                "auditlog",
                "auth_admin_passkey",
                "auth_brute_force",
            ]
            },
        "partner-contact": {
            "_only_": [
                "base_location",
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

    "it-projects-llc": {
        "_only_": ["misc-addons"],
        "misc-addons": {
            "_only_": ["hr_rule_input_compute"]
        }
    }
}
