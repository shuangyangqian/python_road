#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian
# 计算出n + nn + nnn + ....的值，比如 2+22+222+2222


def func(m, n):
    """
    返回 n + nn + nnn + ...的值
    :param m: 表示数字的个数
    :param n: 每个数字中的数
    :return:
    """

    Sn = []
    Tn = 0
    for i in range(1, m+1):
        Tn += n
        n = n * 10
        Sn.append(Tn)
        print Tn
    return Sn


def my_sum(x, y):
    return x + y


Sn = reduce(my_sum, func(5, 4))
print "计算结果是：", Sn




