#!/usr/bin/bash

# author:
# email: shuangyang.qian@easystack.cn
# irc: qsyqian

import time
import logging


def use_logging(func):

    def wrapper(*args, **kwargs):
        logging.info('%s is running' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


@use_logging
def foo(a, b, c):
    t_time = time.strftime('%Y-%m-%d %H:%M:%S')
    print "%s: call foo" % t_time
    print a + b + c


@use_logging
def bar():
    t_time = time.strftime('%Y-%m-%d %H:%M:%S')
    print "%s: call bar" % t_time


foo(1, 2, 3)
bar()
