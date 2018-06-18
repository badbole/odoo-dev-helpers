branch = '10.0'
root = "/opt/odoo/ODOO_10"

clone = {
    '_branch_': '10.0',
    #'_depth_': 1,

    '_skip__': [
        'Odoo'
    ],

    "uvid": {
        # my private working branch, modify per user
        'payroll_oe10': {"_branch_": "10.0-bole"}
    },


    "OCA": {
        "_skip_": ["department", "program", # old versions
                   "server-ux"],
        "currency": {"_branch_": '11.0'}, # examples
        "l10-romaina": {"_branch_": '11.0'}, # examples
        "l10n-croatia": {"_folder_": "oca-l10n-croatia"},
        "oca-decorators": {"_branch_": "master"}, # look like for v8-v10 main decorators
    },
    "vertelab": {
        "odoo-edi": {"_branch_": 'master'},
        "odoo-gdpr": {"_branch_": 'master'},
        "odoo-theme-vertel": {"_branch_": 'master'},
        "odoo-report": {"_branch_": 'master10'},
        "odoo-hr_employercert": {"_branch_": 'master'},
    },
    "decodio": {
        "l10n_hr": {"_branch_": "8.3-dev"},       # examples but for v8
        "community10": {"_branch_": "10.0-dev"},  # collenction of comunity modules from others
    },
    "odoomrp": {
        "odoomrp-wip": {"_branch_": "9.0"},        # for v9
        "odoomrp-utils": {"_branch_": "9.0"}      # for v9
    },
    "asphaltzipper": {
        "azi-odoo-modules": {"_branch_": "master"}
    },
    "ecino": {
        "compassion-modules": {"_branch_": "10.0-emanuel"}
    }

}

sym_dest = "/opt/odoo/ODOO_10/symlink"
symlink = {
    "_info_": 2,
    "_clean_": True,    # default False, clean symlink dir from extras not listed

    "_skip_": [
        "odoo",                         # only special case link!
        "odoomrp",                      # v9.0 modules, TODO port interesting to v10!
        "julius-network-solutions",     # old api.. no like.. leave for examples
        "Smile-SA",                     # interesting concept modules, carefull!!
                                        # - lots of auto_install enabled modules,
                                        # requires update -all as start parameter!
        "ecino",
    ],

    "dajmi5": {
        "_skip_": [
            "d5_odoo_data",             # not needed
            "d5_odoo_demo",             # not needed
        ],
        "l10n_croatia": {
            "_skip_": [
                "l10n_hr_joppd",         # take from uvid repo
                "l10n_hr_bank",          # take from oca repo
                "l10n_hr_base_location", # take from oca repo
            ]
        },
        # "d5_company_kontal": {
        #     "_skip_": [
        #         "object_merger",         # use Julius version, TODO remove from repo!
        #     ]
        # }
    },
    "decodio": {
        "_skip_": [
            "l10n_hr",     # for v8, just for examples
            "community10", # copied from another repos, just examples
        ],

    },
    "OCA": {
        "_skip_": [
            'geospatial',     # need postgis addon on postgres,
            'l10n-italy',     # PyXb - NOPE!!! not wantd!
            "vertical-hotel", # take from Serpent, original author!
            "currency",       # 11
            "server-ux",      # 11
            "connector",
            "l10n-slovenia",  # for v8
        ],
        "account-financial-tools": {
            "_skip_": [
                "currency_rate_update", # take from private d5 repo!
            ]
        },
        "pos": {
            "_skip_": [
                "pos_config",
                "pos_pricelist",
            ]
        },
        "currency": {   # for v11, only examples and ideas!
            "_skip_": [
                "currency_rate_update", # not for 10.0
            ],
        },
        "l10n-croatia": {"_folder_": "oca-l10n-croatia"},
        "oca-decorators": {"_branch_": "master"}, # look like for v8-v10 main decorators

    },
    "brain-tec": {
        "_skip_": [
            "odoo-usability", # forked from Akretion
            "server-tools",   # frk from OCA/server-tools
        ],
    },
    "vertelab": {
        "_skip_": [
            "odoo-edi",   #  no need for now, extra lib : openpyxl
            "odoo-theme-vertel",   # wierd import error! TODO: . check
            "odoo-website",    # lookl like wrong vesion?
        ]
    },
    # "julius-network-solutions": {
    #     "julius-openobject-addons": {
    #         "_skip_": [
    #             "account_followup_choose_partners_2", # some problems starting odoo
    #             "product_tags",                       # yelizarev has better version!
    #             "product_manufacturer",               # use OCA version!
    #         ]
    #     }
    # },


    # "Smile-SA": {
    #     "odoo_addons": {
    #         "_skip_": [
    #             "smile_perf_analyzer",
    #             "smile_audit",
    #             "smile_data_integration",
    #         ]
    #     }
    # },
    "serpent": {
        "SerpentCS_Contributions": {
            "_skip_": [
                "sale_cancel_reason",    # use OCA version
                "partner_credit_limit",   #use Yelizarev version
            ]
        }
    },
    "hibou-io": {
        "hibou-odoo-suite": {
            "_skip_": [
                "hr_payroll_holidays",         # take from hibou-io/odoo-hr-payroll
                "l10n_us_hr_payroll",          # take from hibou-io/odoo-hr-payroll
                "hr_payroll_timesheet",        # take from hibou-io/odoo-hr-payroll
                "l10n_us_hr_payroll_account",  # take from hibou-io/odoo-hr-payroll
                "l10n_us_oh_hr_payroll",       # take from hibou-io/odoo-hr-payroll
                "l10n_us_fl_hr_payroll",       # take from hibou-io/odoo-hr-payroll
                "l10n_us_mo_hr_payroll",       # take from hibou-io/odoo-hr-payroll
                "l10n_us_va_hr_payroll",       # take from hibou-io/odoo-hr-payroll
                "hr_payroll_payment",          # take from hibou-io/odoo-hr-payroll
                "hr_payslip_line_date",        # take from hibou-io/odoo-hr-payroll
            ]
        }
    },
    "it-projects-llc": {
        "partner": {
            "_skip_": [
                "partner_vat_unique",          # use SerpentCS version
            ]
        }
    },
    "Eficent": {
        "ao-odoo": {
            "_skip_": [
                "mrp_production_service",      # use OCA version
            ]
        }
    },
    "Vauxoo": {
        "addons-vauxoo": {
            "_skip_": [
                "partner_credit_limit",   #use Yelizarev version
            ]
        }
    },
    "asphaltzipper": {
        "azi-odoo-modules": {
            "_skip_": [
                "customer_outstanding_statement",  # use OCA version
                "web_notify",
                "account_payment_batch_process",
                "stock_inventory_revaluation",
                "web_search_with_and",
                "partner_daytopay",
                "web_m2x_options",
                "web_sheet_full_width",
            ]
        }
    },
    # "ecino": {
    #     "compassion-modules": {
    #         "_skip_": [
    #             "message_center_compassion"
    #             "child_compassion",  #glupi dependency koji ne radi : jwt
    #         ]
    #     }
    # }
}

pull = {
    '_skip_': ['Odoo'],
    "OCA": {
        "l10n-croatia": {
            "_folder_": "oca-l10n-croatia"
        }
    }
}
