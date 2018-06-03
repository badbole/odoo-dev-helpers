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
root = False

clone = {
    '_branch_': '10.0', # -> if not set, main repo branch will be used
    '_depth_': 1,     # otherwise clone last longer
    # if this is true only these vendors will be processed
    # otherwise, all will be processed with special config per vendor


    """
    reserved keys on vendor|repo level : _skip_, _only_ 
    """
    '_only_': [
        'OCA',
        'Smile-SA',
        'serpent',
        'akretion',
        'brain_tec',
        'studio4it',
    ],

    #"Smile-SA": {}, # will clone all from vendor smile
    "akretion": {
        "_only_":  # only listed repos will be cloned
            ["odoo-usability"]
    },
    "brain-tec": { # all but listed repos will be cloned
        "_skip_": ["server-tools"]
    },
    "OCA": {
        #"_folder_": None,

        "_only_": [
            'server-tools',
            'web',
            'website',
            'l10n-romaina',
            'l10n-croatia'
        ],
        "l10-romaina": {"_branch_": '11.0'},
        "l10n-croatia": {"_folder_": "oca-l10n-croatia"}
    }
}


"""
Main folder containing per config folders with addons symlinks
"""
sym_dest = "/media/data/ODOO_10/symlink"
symlink = {
    "_info_": 2,
    "_clean_": True, #default False, clean symlink dir from extras not listed

    #"_skip_": ["Odoo"],
    "_only_": ['OCA', 'dajmi5'],
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

pull = {
  '_skip_': ['Odoo']
}
