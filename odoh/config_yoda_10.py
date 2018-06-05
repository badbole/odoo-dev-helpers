"""
Prototype odoo helper config
"""


"""
default branch for this config
"""
branch = '10.0'


"""
default location for vendor repos, if not existing, 
current script working directory will be used
"""
root = "/media/data/code/ODOO_10"
sym_dest = "/media/data/ODOO_10/symlink"
symlink = {
    "_info_": 2,
    "_clean_": True, #default False, clean symlink dir from extras not listed

    "_skip_": ["Odoo"],
    #"_only_": ['OCA', 'dajmi5'],
    "OCA": {
        "_skip_": ['geospatial', 'l10n_italy'],
        "account-financial-tools": {
            '_skip_': ['currency_rate_update']
            },
        "pos": {
            "_skip_": ["pos_config", "pos_pricelist"]
            },
    },
}

