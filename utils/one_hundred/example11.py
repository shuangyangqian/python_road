#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian


def rabbit_print(num):
    f1 = 1
    f2 = 2
    for i in range(1, num):
        print "%12d %12d" % (f1, f2)
        f1 = f1 + f2
        f2 = f1 + f2


def rabbit(num):
    """
    this function aim to caculate the results
    :param num:
    :return:
    """
    # 第一个月为1
    f1 = 1
    # 第二个月为1
    f2 = 1

    results = []
    if num == 1:
        results.append(f1)
        print results
    if num == 2:
        # results.append()
        # print results
        print [1, 1]
    else:
        for i in xrange(num-1):
            f1, f2 = f2, f1+f2
    # return f1

rabbit_print(4)
