#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian
# url: https://leetcode.com/problems/two-sum/description/


class Solution(object):

    def twoSum(self, nums, target):
        """
        Return the two number that who's sum is target.

        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        for i in nums:
            for j in nums:
                my_target = i + j
                if my_target == target:
                    return i, j


nums = [2, 33, 44, 55, 7]
target = 35
solution = Solution()
n = solution.twoSum(nums, target)
print n
