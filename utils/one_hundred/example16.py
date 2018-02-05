#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian
# 输出指定格式的日期


import datetime


if __name__ == '__main__':

    # 输出今日日期，格式为dd/mm/yyyy。
    print datetime.date.today().strftime('%d%m%Y')

    # 创建日期对象
    mybirthdate = datetime.date(1992, 9, 16)
    print mybirthdate.strftime("%d%m%Y")

    # 日期算数运算
    mybirthdatenextday = mybirthdate + datetime.timedelta(days=1)
    print mybirthdatenextday.strftime("%d%m%Y")

    # 日期替换
    myfirstbirthday = mybirthdate.replace(year=1901)
    print myfirstbirthday.strftime("%d%m%Y")
