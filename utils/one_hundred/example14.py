#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian
# 将一个数分解质因数，比如输入90，打印出90=2*3*3*5
# 对n进行分解质因数，应该先找到最小的质数k，然后按照下述步骤完成：
# 1：如果这个数恰好等于k，那么结束；
# 2：如果n>k，但是可以被k整除，则打印出k的值，并且使用n除以k的商，作为新的正整数n，重复执行第一步；
# 3：如果n不能被k整除，则使用k+1的值作为k的值，重复执行第一步。


def fen_jie_zhi_yin_shu(n):
    print "{} = ".format(n)
    if not isinstance(n, int) or n < 0:
        print "请输入一个正确的正整数！"
        exit(0)
    elif n in [1]:
        print "{}".format(n)
    while n not in [1]:
        for index in xrange(2, n+1):
            if n % index == 0:
                n = n / index
                if n == 1:
                    print index
                else:
                    print '{} *'.format(index)
                break


fen_jie_zhi_yin_shu(90)




