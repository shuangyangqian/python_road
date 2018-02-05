#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？


def func(hight, mytime):
    hei = hight   # 起始高度
    n = mytime    # 一共多少次
    tour = []     # 总共经过的距离
    height = []   # 最终跳起来的高度
    for i in xrange(1, n + 1):
        if i == 1:
            tour.append(hei)
        else:
            tour.append(2*hei)
        hei /= 2
        height.append(hei)
    return tour, height

a, b = func(100, 10)
print a, b






