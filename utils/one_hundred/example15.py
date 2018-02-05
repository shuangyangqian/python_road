#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian
# 输入分数输出该分数位于的分段，>90分为A，<90并且>70为B，<70并且>60为C，<60输出不及格，请补考。


def func(score):
    if score >= 90:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    else:
        return '不及格，请补考'


score = 120
results = func(score)
print results

