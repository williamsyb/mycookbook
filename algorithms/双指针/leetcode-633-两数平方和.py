# -*- coding UTF-8 -*-
# @project : python03
# @Time    : 2020/6/3 12:34
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : leetcode-633-两数平方和.py
# @Software: PyCharm
import math


class Solution:
    @classmethod
    def judge_square_sum(cls, target):
        if target < 0:
            return False
        i, j = 0, int(math.sqrt(target))
        while i < j:
            res = i * i + j * j
            if res == target:
                print(i, j)
                return True
            elif res < target:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    print(Solution.judge_square_sum(math.pow(34, 2) + math.pow(12, 2)))
