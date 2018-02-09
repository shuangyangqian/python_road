#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian

import os
import shutil

path = './test.txt'


def write_file():
    with open(path, 'wa') as f:
        # content = f.read()
        # print content

        # for line in f.readlines():
        #     print line.strip()
        f.write('\n')
        f.write('this is a hello world')


# 系统相关信息
print os.name
print os.uname()
print os.environ
print os.environ.get('GOROOT')


# 文件目录
print os.path.abspath('./')    # 当前绝对路径
os.mkdir(os.path.join('./', 'testdir'))  # 再当前目录创建一个新目录,当然也可以在制定其他目录下创建
os.rmdir(os.path.join('./', 'testdir'))  # 删除一个目录
print os.path.split('/usr/share/ect/txt.txt')  # 分割文件路径和文件名
# os.rename("aaa", "bbb")  # 重命名
# os.remove('test.txt')  # 删除文件
print os.getcwd()

print [x for x in os.listdir('.') if os.path.isdir(x)]  # 列出当前目录下的所有目录
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']  # 列出当前目录下所有的py文件