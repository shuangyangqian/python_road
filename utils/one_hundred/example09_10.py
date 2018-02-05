#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian


import time

a = {"name": "sqian", "age": 26, "sex": "male", "high": 173}
for key, value in dict.items(a):
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print key, value
    time.sleep(2)
