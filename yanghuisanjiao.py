#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian

# 使用Python写出一个n行的杨辉三角形
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 3 1
# ......


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n-1] for n in range(1, len(L))] + [1]


n = 0
for t in triangles():
    print t
    n = n + 1
    if n == 10:
        break
