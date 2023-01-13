#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Bene
# @Time    : 2022/2/9 18:13
# @File    : Log.py
# @Function: 日志服务
# ====#====#====#====
import logging
import os
import platform
import time
from datetime import datetime


def get_file_path(DirectoryName, file_path):
    """
    @param DirectoryName:  文件目录
    @param file_path:  文件名
    @return: 文件绝对路径
    """
    Dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + r"%s" % DirectoryName)
    dir_name = Dir_path + "/" + file_path
    if platform.system() == 'Windows':
        return dir_name.replace('/', '\\')
    else:
        return dir_name


LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'
today = datetime.now().strftime('%Y-%m-%d')


def set_handler(levels):
    if levels == 'error':
        logger.addHandler(Log.handler)
    logger.addHandler(Log.handler)


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(Log.handler)
    logger.removeHandler(Log.handler)


# 创建文件
def create_file(file_name):
    path = file_name[0:file_name.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(file_name):
        with open(file_name, 'w', encoding='utf-8') as fd:
            fd.write(file_name)


def get_current_time():
    return time.strftime(Log.date, time.localtime(time.time()))


class Log:
    report_path = '/Log' + '/' + today
    log_file = get_file_path(report_path, "log_file.log")
    # err_file = get_file_path(report_path, "err_file.log")
    logger.setLevel(LEVELS.get(level, logging.INFO))
    create_file(log_file)
    # create_file(err_file)
    date = '%Y-%m-%d %H:%M:%S'
    handler = logging.FileHandler(log_file, encoding='utf-8')
    # err_handler = logging.FileHandler(err_file, encoding='utf-8')

    @staticmethod
    def debug(*log_msg):
        set_handler('debug')
        logger.debug('[DEBUG ' + get_current_time() + ']' + merge_msg(*log_msg))
        remove_handler('debug')

    @staticmethod
    def info(*log_msg):
        set_handler('info')
        logger.info('[INFO ' + get_current_time() + ']' + merge_msg(*log_msg))
        remove_handler('info')

    @staticmethod
    def warning(*log_msg):
        set_handler('warning')
        logger.warning('[WARNING ' + get_current_time() + ']' + merge_msg(*log_msg))
        remove_handler('warning')

    @staticmethod
    def error(*log_msg):
        set_handler('error')
        logger.error('[ERROR ' + get_current_time() + ']' + merge_msg(*log_msg))
        remove_handler('error')

    @staticmethod
    def critical(*log_msg):
        set_handler('critical')
        logger.critical('[CRITICAL ' + get_current_time() + ']' + merge_msg(*log_msg))
        remove_handler('critical')


def merge_msg(*msg):
    res = ' '.join(list(map(lambda x: str(x), msg)))
    return res


if __name__ == "__main__":
    Log.debug("This is debug message", 'debug')
    Log.info("This is info message", 'info')
    Log.warning("This is warning message", 'waring')
    Log.error("This is error", 'error')
    Log.critical("This is critical message", 'critical')
