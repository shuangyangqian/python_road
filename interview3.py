#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time


def my_time(func):
    def wrapper(*args, **kwargs):
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return func(*args, **kwargs)
    return wrapper


@my_time
def fib(n):

    if n <= 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


@my_time
def fib_2(n):
    i = 1
    j = 1
    results = []
    while 0 < i < 10000000:
        i, j = j, i+j
        results.append(i)
    return results[n]

n = fib_2(10)
print n

# n = fib(10)
# print n
