#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 文件内容是 aaa
#           bbb
#           ccc
# 打印出  nova delete aaa
#        nova delete bbb

my_file = open("1.txt", 'r')
for line in my_file.readlines():
    print "nova delete " + line
my_file.close()
