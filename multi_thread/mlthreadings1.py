#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian


import threading

lock = threading.Lock()


def print_it(name):
    lock.acquire()
    try:
        for i in range(100000):
            print "this is %s" % name
    finally:
        lock.release()


def run_thread(name):
    print_it(name)


t1 = threading.Thread(target=run_thread, args=("qian", ))
t2 = threading.Thread(target=run_thread, args=("shuang", ))
t3 = threading.Thread(target=run_thread, args=("yang", ))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()