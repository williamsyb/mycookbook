# -*- coding UTF-8 -*-
# @project : python03
# @Time    : 2020/6/3 12:18
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : leetcode-167-有序数组的TwoSum.py
# @Software: PyCharm

# 有序数组的Two Sum
"""
Input: numbers={2,7,11,15}, target=9
Output: index1=1,index2=2
"""


class Solution:
    @classmethod
    def two_sum(cls, numbers: list, target: int):
        """
        时间复杂度O(n),只循环了一轮；只使用了两个额外空间，空间复杂度O(1)
        """
        if numbers is None:
            return None
        i, j = 0, len(numbers)-1  # 使用两个索引指针
        while i < j:
            sum_ = numbers[i] + numbers[j]
            if sum_ == target:
                return [i + 1, j + 1]
            elif sum_ < target:
                i += 1
            else:
                j -= 1
        return None


if __name__ == '__main__':
    li = [6, 78, 90, 110, 234, 678]
    print(Solution.two_sum(li, 84))
