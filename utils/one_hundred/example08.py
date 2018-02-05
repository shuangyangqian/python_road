#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian


def nine_nine():
    for i in range(1, 10):
        results = []
        for j in range(1, i+1):
            a = "%d*%d=%d" % (i, j, i*j)
            results.append(a)
        print results
nine_nine()
