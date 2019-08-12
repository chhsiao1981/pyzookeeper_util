# -*- coding: utf-8 -*-

import argparse

from . import cfg
from . import util


def get_acls(path, zkCli, server, config=None, auth=None):
    cmd = 'getAcl %s' % (path)

    auth_str = util.auth_to_auth_str(auth)

    stdout_list, stderr_list = util.exec(cmd, zkCli, server, config, auth_str)

    valid_stdout_list = util.filter_valid_list(stdout_list, ["'sasl", "'world", "'digest", ':'])

    if len(valid_stdout_list) % 2 != 0:
        cfg.logger.error('get_acls: not parse correctly: valid_stdout_list: %s', valid_stdout_list)
        return []

    acls = [''.join(valid_stdout_list[i:i + 2]).replace("'", '').replace(',', ':').replace(' ', '') for i in range(0, len(valid_stdout_list), 2)]

    return acls


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

    acls = get_acls(path, zkCli, server, config, auth)

    cfg.logger.info('after get_acls: path: %s acls: %s', path, acls)


if __name__ == '__main__':
    _main()
