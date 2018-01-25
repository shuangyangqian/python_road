#!/usr/bin/python
#coding=utf-8

# author:
# email: shuangyang.qian@easystack.cn
# irc: qsyqian

import time
import os
import sched

schedule =sched.scheduler(time.time, time.sleep)


def perform_command(cmd, inc):
    os.system()


def timming_exe(cmd, inc=60):
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    schedule.run()


print "show time after 10 seconds:"
timming_exe("echo %time%", 10)
