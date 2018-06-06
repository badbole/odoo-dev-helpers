#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: bole@dajmi5.com


import os
import subprocess
# import datetime
import ast
import argparse


class ConfigHandler(object):

    def __init__(self, config):
        self.config = {}
        self.__setattr__('conf_name', config)
        self.config_defaults = {
            'clone': {
                '_branch_': False,
                '_depth_': False,
                '_folder_': False
            },
            'symlink': {
                '_folder_': False,

            }
        }
        if config:
            try:
                c = __import__("config_" + config)
            except Exception as E:
                print "ERROR : " + E

            for option in dir(c):
                if option.startswith('__'):
                    continue
                try:
                    opt = eval("c." + option)
                    self.config.update({option: opt})
                except Exception as E:
                    print E

        if not self.config.get('root'):
            self.config.update({
                'root': os.path.join(os.getcwd(), 'CODE_GARAGE')
            })

    def _get_unders(self, config):
        res = {}
        for key in config:
            if key.endswith('_') or key.startswith('_'):
                res.update({key: config[key]})
        return res


class RepoHandler(ConfigHandler):
    """
    Handler for repositories configured
    """

    def _get_name_from_link(self, link):
        if 'http' in link:
            # htts|s
            link = link.split('/')
            #repo = link[-1]
            vendor = link[-2]
        elif '@' in link:
            # ssh
            link = link.split(':')
                #.split('/')
            try:
                vendor = link[1].replace('/', '')
            except Exception as E:
                print E

            #vendor = vendor.replace('/', '')

        else:
            vendor = False
        return vendor

    def __init__(self, args):

        super(RepoHandler, self).__init__(args.get('config'))
        structure = []

        for file in os.listdir(os.getcwd()):
            file_list = []

            if file.startswith('group'):
                try:
                    cr = __import__(file.replace('.py', ''))
                except Exception as E:
                    cr = False
                    pass
                if cr:
                    file_list.append(file)
                    group = file.replace('group_', '').replace('.py', '')
                    vendors = []
                    for vendor in cr.odoo:
                        vendor_folder = vendor.get('folder')
                        if not vendor_folder:
                            vendor_folder = self._get_name_from_link(link=str(vendor.get('link')))
                                        #vendor.get('link')[:-1].split('/')[-1]
                        vals = {
                            'path': vendor_folder,
                            'link': vendor.get('link'),
                            'repos': vendor.get('repos'),
                            'comment': vendor.get('comment')
                        }
                        vendors.append(vals)
                        #self.groups.__setattr__(vendor_folder, vals)
                    structure.append((group, vendors))

                    #self._folders.append(file)
        self.structure = structure
        self._actions = []

        self.process_group(args)
        pass

    def _check_skip(self, path, defaults):
        res = False
        if defaults.get('_skip_') and path in defaults['_skip_'] or \
           defaults.get('_only_') and path not in defaults['_only_']:
            res = True
        return res

    def process_group(self, args):
        conf_main = eval("self.config['" + args.get('action') + "']")
        for group_folder, group_vendors in self.structure:
            path = group_folder
            defaults = self._get_unders(conf_main)
            for vendor in group_vendors:
                v_path = vendor['path']
                if self._check_skip(v_path, defaults):
                    continue
                conf_vendor = conf_main.get(v_path, {})
                defaults_vendor = self._get_unders(conf_vendor)
                folder_corr = defaults_vendor.get('_folder_', False)
                if folder_corr:
                    v_path = folder_corr
                else:
                    pass
                vals = {
                    'path': [path, vendor['path']],
                    'real_path': [path, v_path],
                    'defaults': defaults,
                    'vendor': vendor,
                    'conf_vendor': conf_vendor,
                    'default_vendor': defaults_vendor
                }
                self.process_vendor_repos(conf_main, vals)

    def _get_defaults(self, conf):
        vals = {}
        for key in conf:
            if key in ('_skip_', '_only_'):
                continue
            vals.update({key[1:-1]: conf[key]})
        return vals

    def process_vendor_repos(self, conf, vals):  # conf_vendor, defaults, vendor, v_path):
        real_path = vals['real_path']
        vendor_repos = vals['vendor']['repos']
        for repo in vendor_repos:
            if self._check_skip(repo, vals['default_vendor']):
                continue

            # if 'decodio' in vals['vendor']['link']:
            #     # catch only
            #     pass
            path = list(vals['path'])
            path.append(repo)
            my_path = list(real_path)
            try:
                cr = vals['conf_vendor'].get(repo, False)
            except Exception as E:
                cr = False
                print E
            if cr:

                folder_repo = cr.get('_folder_') and cr['_folder_'] or False
                if folder_repo:
                    my_path.append(folder_repo)
                else:
                    my_path.append(repo)

                rep_vals = self._get_defaults(cr)
            else:
                my_path.append(repo)
                rep_vals = {}
                pass

            if self.action == 'clone':
                def_vals = self._get_defaults(vals['defaults'])
                ven_vals = self._get_defaults((vals['default_vendor']))
                my_val = {}
                for val in [def_vals, ven_vals, rep_vals]:
                    if not val:
                        continue
                    for key in val:
                        if key == 'folder':
                            continue
                        my_val[key] = val[key]
                my_val['path'] = path
                my_val['my_path'] = my_path
                my_val['link'] = vals['vendor']['link']
                #print my_val
                self._actions.append((my_val))
            elif self.action == 'symlink':
                check_folder = '/'.join([self.config['root']] + my_path)
                folder_repos = []

                if os.path.exists(check_folder):
                    folder_repos = [
                        r for r in os.listdir(check_folder)
                        if os.path.isdir(os.path.join(check_folder, r)) \
                        and r not in ['.idea', '.git', 'setup']
                    ]  # TODO: add eclipse config folder?
                else:
                    pass


                do_repos = []
                for r in folder_repos:
                    if cr and self._check_skip(r, cr):
                        continue
                    do_repos.append(r)
                if do_repos:
                    self._actions.append([check_folder, do_repos])

            elif self.action == 'pull':
                repo = '/'.join(([self.config['root']] + my_path))
                self._actions.append(repo)


class Manager(RepoHandler):
    """
    Odoo developer helper

    assuming you have git already set up
       - using global or local config, or registred ssh key

    config files: group_*
       -

    """

    def __init__(self, args):
        action = args.get('action')
        if not action:
            print "No action defined"
            exit(0)
        self.action = action
        super(Manager, self).__init__(args)
        eval("self.%s()" % action)

    def check_create_folder(self, path):
        if not os.path.exists(path):
            print "Create folder : " + path
            os.mkdir(path)
        return path

    def _run_shell(self, command):
        run = subprocess.Popen(command, stderr=subprocess.PIPE)
        out, err = run.communicate()
        ok = False
        if err.endswith('...\n'):
            err = err.replace('...\n', '... OK')
            ok = True
        else:
            pass
        return ok, err

    def clone(self):
        root = self.check_create_folder(self.config['root'])
        for action in self._actions:
            git = ['git', 'clone']
            repo = ''.join((action['link'], action['path'][-1], '.git'))
            git.append(repo)
            if action.get('branch'):
                if 'master' != action['branch']:
                    git.append('--branch=%s' % action['branch'])
            if action.get('depth'):
                git.append('--depth=%s' % action['depth'])
            repo_path = root
            for path in action['my_path'][:-1]:
                repo_path = self.check_create_folder('/'.join((repo_path, path)))
            git_path = '/'.join((repo_path, action['my_path'][-1]))
            if os.path.exists(git_path) and \
                os.path.exists(git_path + '/.git'):
                print "Repo %s aldready present" % repo
                continue
            git.append(git_path)
            ok, err = self._run_shell(git)
            if not ok:
                if "could not read Username for 'https://github.com'" in err:
                    print "Please run git config and restart script"
                elif "Could not find remote branch" in err:
                    print "Could not find remote branch : %s" % action['branch']
                    # new = []
                    # for c in git:
                    #     new.append(c)
                    #     if '.git' in c:
                    #         break
                    # print err
                    # print " Try master"
                    # ok, err = self._run(new)
                    # if not ok:
                    #     pass
                else:
                    pass
            else:
                pass

            print err

    def pull(self):
        for repo in self._actions:
            if os.path.exists(repo):
                os.chdir(repo)
                print "Pull : ", repo
                ok, err = self._run_shell(['git', 'pull'])
                if err:
                    print err
            else:
                print "Not existing path : ", repo

    def _check_installabile(self, module_path):
        installable = False
        for man in ('__manifest__.py', '__openerp__.py'):
            manifest_path = os.path.join(module_path, man)
            if os.path.exists(manifest_path):
                try:
                    manifest = ast.literal_eval(open(manifest_path).read())
                    installable = manifest.get('installable', True)
                except:
                    print "--> Error reading module : ", module_path
                return installable
        print "--> No manifest in folder : %s" % module_path
        return installable

    def _installabile_modules(self):
        installable = []
        for root, repos in self._actions:
            for repo in repos:
                r = '/'.join((root, repo))
                is_instllable = self._check_installabile(r)
                if is_instllable:
                    installable.append((root, repo))
        return installable

    def symlink(self):
        installable = self._installabile_modules()
        dest_root = self.check_create_folder(self.config['sym_dest'])
        dest_symlink = self.check_create_folder('/'.join((dest_root, self.conf_name)))
        existing = {}
        done = {'created': {}, 'modified': {}, 'ok': {}}
        for path, files, folders in os.walk(dest_symlink):
            for file in files:
                fpath = '/'.join((path, file))
                if os.path.islink(fpath):
                    existing[fpath] = os.readlink(fpath)
        full_existing = dict(existing)
        for path, module in installable:
            src = '/'.join((path, module))
            dst = '/'.join((dest_symlink, module))
            dst_exist = existing.get(dst, False)
            if not dst_exist:
                if not full_existing.get(dst, False):
                    try:
                        os.symlink(src, dst)
                        done['created'][dst] = src
                        full_existing[dst] = src
                    except Exception as E:
                        pass
                    continue
                else:
                    pass
            if dst_exist == src:
                done['ok'][dst] = src
            else:
                os.remove(dst)
                os.symlink(src, dst)
                done['modified'][dst] = (src, dst_exist)
                continue
        clean = self.config['symlink'].get('_clean_', False)
        if clean:
            ok = dict(done['created'])
            ok.update(done['modified'])
            ok.update(done['ok'])
            to_remove = []
            for link in existing:
                if link not in ok:
                    to_remove.append(link)
            for r in to_remove:
                os.remove(r)
        if done['created']:
            print "created : ", len(done['created'])
        if done['modified']:
            print "modified : ", len(done['modified'])
        if done['ok']:
            print "ok : ", len(done['ok'])
        if clean and to_remove:
            print "removed : ", len(to_remove)


if __name__ == '__main__':
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
