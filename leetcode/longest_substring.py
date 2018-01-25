#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian
# url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """

        :param s:
        :return:
        """

        substr = []

        if len(s) == 1:
            return 1
        i = 0
        j = 1
        while i <= len(s) - 1:
            while j <= len(s):
                if s[j] not in s[i:j]:
                    if j == len(s) - 1:
                        if len(substr) < len(s[i:j + 1]):
                            substr = s[i:j + 1]
                        return len(substr)
                    j += 1
                else:
                    if len(s[i:j]) > len(substr):
                        substr = s[i:j]
                    i += 1
        return len(substr)


str = "qw"
s = Solution()
n = s.lengthOfLongestSubstring(str)
print n
