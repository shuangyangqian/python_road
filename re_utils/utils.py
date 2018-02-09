#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian

# [0-9a-zA-Z\_]   一个数字,字母或下划线
# [0-9a-zA-Z\_]+  至少一个数字或者字母与下划线组成的字符创
# [a-zA-Z\_][0-9a-zA-Z\_]* 字母或者下划线开头,后接由数字字母下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]{0,19}  准确限制了字符的数目 20个
# (P|p)ython  用来匹配python 或者Python
# ^表示行的开头  ^\d表示必须以数字开头
# $表示行的结尾 \d$表示必须以数字结尾


import re


def phone_re():
    re_phone = r"^(\d{3}\)-(\d{3,8})$"
    flag = re.match(re_phone, "010-1231234123")
    return flag.groups()


def is_valid_email(addr):
    # key = r'[0-9a-zA-Z\_]+@[0-9a-zA-Z\_]+(\.[com|cn])]'
    key = r'python'
    re_email = re.compile(key)
    macher = re_email.findall(addr)
    return macher


def spilt_util(name):
    return re.split(r'\s+,', name)


print is_valid_email(r"pythonjavacgolang")
