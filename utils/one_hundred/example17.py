#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian
#


def func(my_str):
    i = 0
    j = 0
    k = 0
    for n in my_str:
        if n.isalpha():
            i += 1
        elif n.isdigit():
            j += 1
        elif n.isspace():
            k += 1
    return i, j, k


my_str = "asfd afhdueiosfr haslmkdfn ;iha gyhiofgtqwehgklajsdnfg klsagh rwiueohfg"
string_num, digit_num, space_num = func(my_str)
print "字母有 %d 个。" % string_num
print "数字有 %d 个。" % digit_num
print "空格有 %d 个。" % space_num
