#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian

# 总共有n台阶梯,一个人一次可以跳一级阶梯,也可以一次跳两次阶梯,问总共有多少种跳法
# 比如　1-->1
#      2-->2 (1,1) (2)
#      3-->3 (1,1,1) (1,2) (2,1)


def claimStairs(n):

    if n == 1:
        results = 1
        return results
    elif n == 2:
        results = 2
        return results
    elif n >= 3:
        results = claimStairs(n-1) + claimStairs(n-2)
        return results


a = claimStairs(5)
print a
