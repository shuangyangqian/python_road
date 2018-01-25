#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian


for i in range(1, 5):
    for j in range(1, 5):
        if i == j:
            continue
        for k in range(1, 5):
            if k == i or k == j:
                continue
            print i, j, k
