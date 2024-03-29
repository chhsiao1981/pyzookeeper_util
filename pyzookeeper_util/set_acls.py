# -*- coding: utf-8 -*-

import argparse

from . import cfg
from . import util
from .get_acls import get_acls


def set_acls(path, acls, zkCli, server, config=None, auth=None):
    cmd = 'setAcl %s %s' % (path, ','.join(acls))

    auth_str = util.auth_to_auth_str(auth)

    cfg.logger.debug('set_acls: to exec: cmd: %s auth_str: %s', cmd, auth_str)
    stdout_list, stderr_list = util.exec(cmd, zkCli, server, config, auth_str)

    return None if not stderr_list else stderr_list


def parse_args():
    ''' '''
    parser = argparse.ArgumentParser(description='zookeeper_util: get_children')
    parser.add_argument('-i', '--ini', type=str, required=True, help="ini filename")
    parser.add_argument('-p', '--path', type=str, required=True, help="path")
    parser.add_argument('-a', '--acls', type=str, required=True, help="acls")
    parser.add_argument('-l', '--log_filename', type=str, default='', required=False, help="log filename")

    args = parser.parse_args()

    return None, args


def _main():
    error, args = parse_args()
    cfg.init(args.ini, args.log_filename)

    path = args.path
    acls = args.acls.split(',')

    zkCli = cfg.config.get('zkcli', None)
    server = cfg.config.get('server', None)
    config = cfg.config.get('config', None)
    auth = cfg.config.get('auth', None)

    orig_acls = get_acls(path, zkCli, server, config, auth)
    ret = set_acls(path, acls, zkCli, server, config, auth)
    new_acls = get_acls(path, zkCli, server, config, auth)

    cfg.logger.info('after set_acls: path: %s acls: %s ret: %s orig_acls: %s new_acls: %s', path, acls, ret, orig_acls, new_acls)


if __name__ == '__main__':
    _main()
