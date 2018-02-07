#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian


import threading

local_school = threading.local()
lock = threading.Lock()


class Student(object):

    def __int__(self, name):
        print "hello %s" % name


def process_student():
    for i in range(1000000):
        lock.acquire()
        try:
            print "Hello, %s (in %s)" % (local_school.student, threading.current_thread().name)
        finally:
            lock.release()


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=("qianshuangyang", ), name="Th-1")
t2 = threading.Thread(target=process_thread, args=("sqian", ), name="Th-2")
t1.start()
t2.start()
t1.join()
t2.join()