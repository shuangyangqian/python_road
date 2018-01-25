#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian
# url: https://leetcode.com/problems/add-two-numbers/description/


class Node(object):

    def __init__(self, value, nextnode=None):
        self.value = value
        self._nextnode = nextnode

    def append(self, n):
        if not isinstance(n, Node):
            n = Node(n)
        self._nextnode, n = n, self._nextnode
        self._nextnode._nextnode = n


class Solution(object):

    def addTwoNumber(self, l1, l2):
        """

        :param l1: Listnode
        :param l2: Listnode
        :return: ListNode
        """
        pass


n = Node(7)
n.append(8)
n.append(9)
for i in n:
    print i
