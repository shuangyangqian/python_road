#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian
# 判断101到200之间有多少个素数 并且输出这些素数
# 素数评判标准： 用2到sqrt（该数）来整除这个数，如果都不能整除，则为素数，否则不是


from math import sqrt


def su_shu_print(x, y):
    h = 0
    leap = 1
    results = []
    for i in range(x, y):
        k = int(sqrt(i))
        for j in range(2, k+1):
            if i % j == 0:
                leap = 0
                break
        if leap == 1:
            # print "%d" % i
            h = h + 1
            results.append(i)

        leap = 1
    return results, h


l, n = su_shu_print(100, 200)
print l
print n
