#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian
# 打印出水仙花数，水仙花数类似于153，因为153=1三次方+5三次方+3三次方


def shui_xian_hua_print(x, y):
    results = []
    for n in range(x, y):
        i = n / 100
        j = n / 10 % 10
        k = n % 10
        if n == i**i + j**3 + k**3:
            results.append(n)

    return results

l = shui_xian_hua_print(1, 999)
print l



