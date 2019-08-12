# -*- coding: utf-8 -*-

import argparse

from . import cfg
from . import util


def get_children(path, zkCli, server, config=None, auth=None):
    cmd = 'ls -R %s' % (path)

    auth_str = util.auth_to_auth_str(auth)

    stdout_list, stderr_list = util.exec(cmd, zkCli, server, config, auth_str)

    children = util.filter_valid_list(stdout_list, ['/'])

    return children


def parse_args():
    ''' '''
    parser = argparse.ArgumentParser(description='zookeeper_util: get_children')
    parser.add_argument('-i', '--ini', type=str, required=True, help="ini filename")
    parser.add_argument('-p', '--path', type=str, required=True, help="path")
    parser.add_argument('-l', '--log_filename', type=str, default='', required=False, help="log filename")

    args = parser.parse_args()

    return None, args


def _main():
    error, args = parse_args()
    cfg.init(args.ini, args.log_filename)

    path = args.path

    zkCli = cfg.config.get('zkcli', None)
    server = cfg.config.get('server', None)
    config = cfg.config.get('config', None)
    auth = cfg.config.get('auth', None)

    children = get_children(path, zkCli, server, config, auth)

    cfg.logger.info('after get_children: path: %s children: %s', path, children)


if __name__ == '__main__':
    _main()
