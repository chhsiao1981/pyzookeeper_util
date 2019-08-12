# -*- coding: utf-8 -*-

from io import StringIO

from subprocess import Popen, PIPE


def exec(cmd, zkCli, server, config=None, auth=None):
    cmds = []
    if auth is not None:
        cmds.append(auth)
    cmds += [cmd, 'quit']
    cmds_str = '\n'.join(cmds)
    cmd_io = StringIO(cmds_str)

    pcmd = [
        zkCli,
        '-server',
        server,
    ]

    if config is not None:
        pcmd += ['--config', config]

    process = Popen(pcmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate(cmd_io.read().encode('utf-8'))
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')
    stdout_list = stdout.split('\n')
    stderr_list = stderr.split('\n')

    return stdout_list, stderr_list


def auth_to_auth_str(auth):
    auth_list = auth.split(':')
    return ' '.join([auth_list[0], ':'.join(auth_list[1:])])


def filter_valid_list(the_list, valid_starts):
    def _filter(x):
        for each in valid_starts:
            if x.startswith(each):
                return True
        return False

    return list(filter(_filter, the_list))
