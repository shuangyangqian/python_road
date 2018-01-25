#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian


import sys


if __name__ == "__main__":
    target_server = sys.argv[1]
    password = sys.argv[2]
    auto_ssh(target_server, password)


def auto_ssh(server, password):
    cmd = "ssh root@%s" % server

