branch = '10.0'
root = "/media/data/code/ODOO_10"

clone = {
    '_branch_': '10.0',
    #'_depth_': 1,

    '_skip__': ['Odoo'],

    "uvid": {
        # my private working branch, modify per user
        'payroll_oe10': {"_branch_": "10.0-bole"}
    },


    "OCA": {
        "_skip_": ["department", "program", # old versions
                   "server-ux"],
        "currency": {"_branch_": '11.0'}, # examples
        "l10-romaina": {"_branch_": '11.0'}, # examples
        "l10n-croatia": {"_folder_": "oca-l10n-croatia"}
    },
    "vertelab": {
        "odoo-edi": {"_branch_": 'master'},
        "odoo-gdpr": {"_branch_": 'master'},
        "odoo-theme-vertel": {"_branch_": 'master'},
        "odoo-report": {"_branch_": 'master10'},
        "odoo-hr_employercert": {"_branch_": 'master'},
    },
    "decodio": {
        "l10n_hr": {"_branch_": "8.3-dev"} # examples1
    }
}

sym_dest = "/media/data/code/ODOO_10/symlink"
symlink = {
    "_info_": 2,
    "_clean_": True, #default False, clean symlink dir from extras not listed

    "_skip_": ["Odoo"],
    #"_only_": ['OCA', 'dajmi5'],
    "dajmi5": {
        "_skip_": [
            "d5_odoo_data",
            "d5_odoo_demo",
        ],
        "l10n_croatia": {
            "_skip_": [
                "l10n_hr_joppd", # uvid repo
                "l10n_hr_bank",  # oca repo
                "l10n_hr_base_location",
            ]
        }
    },
    "decodio": {
        "_skip_": [
            "l10n_hr",
            "comunity10"
        ],

    },
    "OCA": {
        "_skip_": ['geospatial', 'l10n_italy'],
        "account-financial-tools": {
            '_skip_': [
                'currency_rate_update'
            ]
        },
        "pos": {
            "_skip_": [
                "pos_config",
                "pos_pricelist"
            ]
        },
    },
}

pull = {
  '_skip_': ['Odoo']
}
