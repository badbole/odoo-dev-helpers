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
        "CybroOdoo",
        "it-projects-llc",
        "akretion",
        "ecino",
        "abakus-it"
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
    "ecino": {
        "_only_": ["compassion-modules"],
        "compassion-modules": {
            "_only_": [
                "hr_attendance_calendar",
                "hr_attendance_extra_hours",
                "hr_planning",
            ]
        },
    },
    "abakus-it": {
        "_only_": ["hr"],

    },
    "akretion": {
        "_only_": ["odoo-usability"],
        "odoo-usability": {
            "_only_": [
                "hr_holidays_usability",
                "hr_usability",
            ]
        }
    },
    "OCA": {
        "_only_": [
            'server-tools',
            'partner-contact',
            'web',
            "l10n-croatia",
            "hr",
            "hr-timesheet",
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
                "partner_firstname"
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
        },
        # "hr": {
        #     "_only_": [
        #         "hr_contract_default_trial_length",
        #         "hr_emergency_contact",
        #         "hr_employee_birth_name",
        #         "hr_employee_firstname",
        #         "hr_employee_social_media",
        #         "hr_family",
        #         "hr_holidays_compute_days",
        #         "hr_holidays_imposed_days",
        #         "hr_holidays_legal_leave",
        #         "hr_holidays_notify_employee_manager",
        #         "hr_holidays_settings",
        #         "hr_holidays_validity_date",
        #         "hr_public_holidays",
        #         "hr_recruitment_skill",
        #         "hr_skill",
        #         "hr_worked_days_from_timesheet",
        #
        #     ]
        # },
    },

    "CybroOdoo": { # 15.6.18
        "CybroAddons": {
            "_only_": [
                "employee_creation_from_user",
                "employee_document_expiry",
                "hr_custody",
                "hr_employee_attendance",
                "hr_insurance",
                "hr_linkedin_recruitment",
                "hr_payslip_monthly_report",
                "hr_resignation",
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
