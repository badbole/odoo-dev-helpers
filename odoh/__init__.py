#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: bole@dajmi5.com


import argparse
from main import Manager



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="odoh", description='Odoo helper functions',
        epilog="""
            For more info call help on each option :
            odoh symlink -h
            """)
    parser.add_argument('action', help='Repo action')
    #parser.add_argument('-a', '--action', nargs='+', help='Repos actions')
    parser.add_argument('-c', '--config', help=' optional custom config to run')

    parser.add_argument('-r', '--repos', nargs='+', help='Repos config for run')

    args = vars(parser.parse_args())
    manager = Manager(args)
    # manager.process()
