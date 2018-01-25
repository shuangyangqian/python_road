#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian


def get_day(date):
    a, b, c = date.split("-")
    year = int(a)
    month = int(b)
    day = int(c)

    months = [0, 31, 59, 90, 120, 151, 181, 212,
              243, 273, 304, 334]
    if 0 < month <= 12:
        result = months[month - 1]
    else:
        print "data error"

    result += day
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if leap == 1 and month > 2:
        result += 1
    return result


result = get_day("2018-09-22")
print result

