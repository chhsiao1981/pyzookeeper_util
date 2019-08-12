# -*- coding: utf-8 -*-

import argparse

from . import cfg
from . import util
from .get_children import get_children


def recursive_get_acls(path, zkCli, server, config=None, auth=None):
    children = get_children(path, zkCli, server, config, auth)

    results = {each: get_acls(each, zkCli, server, config, auth) for each in children}

    return results


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

    results = recursive_get_acls(path, zkCli, server, config, auth)

    children = results.keys()
    for idx, each in enumerate(children):
        cfg.logger.info('(%s/%s): %s: %s', idx, len(children), each, results[each])


if __name__ == '__main__':
    _main()
