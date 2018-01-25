#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian

import MySQLdb

conn = MySQLdb.Connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='passw0rd'
                       )
