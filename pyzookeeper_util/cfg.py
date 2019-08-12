# -*- coding: utf-8 -*-

from configparser import SafeConfigParser
import logging
import logging.config
import ujson as json

# global variables
logger = None
config = None

# internal global variables

_NAME = "zookeeper_util"


def init(ini_filename, log_ini_filename='', params=None):
    _init_logger(log_ini_filename, ini_filename)
    _init_ini_file(ini_filename)
    _post_init_config(params)


def _init_logger(log_ini_filename, ini_filename):
    global logger
    logger = logging.getLogger(_NAME)

    if not log_ini_filename:
        log_ini_filename = ini_filename

    if not log_ini_filename:
        return

    logging.config.fileConfig(log_ini_filename, disable_existing_loggers=False)


def _init_ini_file(ini_filename):
    '''
    setup rx_med_analysis:main config
    '''
    global config

    section = _NAME + ':main'

    config = _init_ini_file_core(ini_filename, section)


def _init_ini_file_core(ini_filename, section):
    '''
    get ini conf from section
    return: config: {key: val} val: json_loaded
    '''
    config_parser = SafeConfigParser()
    config_parser.read(ini_filename)
    options = config_parser.options(section)
    logger.info('ini_filename: %s section: %s options: %s', ini_filename, section, options)
    config = {option: _init_ini_file_parse_option(option, section, config_parser) for option in options}

    return config


def _init_ini_file_parse_option(option, section, config_parser):
    try:
        val = config_parser.get(section, option)
    except Exception as e:
        logger.exception('unable to get option: section: %s option: %s e: %s', section, option, e)
        val = ''
    return _init_ini_file_val_to_json(val)


def _init_ini_file_val_to_json(val):
    '''
    try to do json load on value
    '''

    if val.__class__.__name__ != 'str':
        return val

    orig_v = val
    try:
        val = json.loads(val)
    except:
        val = orig_v

    return val


def _post_init_config(params):
    '''
    add additional parameters into config
    '''
    global config

    for (k, v) in params.items():
        if k in config:
            logger.warning('params will be overwrite: key: %s origin: %s new: %s', k, config[k], v)

    config.update(params)

    logger.debug('_post_init_config: done: config: %s', config)
