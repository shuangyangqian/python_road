#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 数组去重


def func(my_list):
    my_list2 = []
    for i in my_list:
        if i not in my_list2:
            my_list2.append(i)
    return my_list2


l = func([1, 1, 1, 1, 2, 2, 2, 2])
print l
