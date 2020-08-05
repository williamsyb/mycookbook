# -*- coding UTF-8 -*-
# @project : python03
# @Time    : 2020/7/22 11:15
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : 最长子序和.py
# @Software: PyCharm
import sys


class Solution:
    @staticmethod
    def solution(arr):
        ans, maxn = 0, -sys.maxsize
        size = len(arr)
        for i in range(size):
            if ans < 0:
                ans = 0
            ans += arr[i]
            maxn = max(maxn, ans)
        return maxn
