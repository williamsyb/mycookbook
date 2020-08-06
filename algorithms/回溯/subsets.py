from typing import List
from pprint import pprint

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        result = []

        def backtrack(start, capital, route=[]):
            if len(route) == capital:
                result.append(route.copy())
                return
            for i in range(start, size):
                route.append(nums[i])
                new_start_index = i + 1
                backtrack(new_start_index, capital)
                route.pop()
            return

        for capital in range(size + 1):
            start_index = 0
            backtrack(start_index, capital)
        return result














def solution(arr):
    results = []
    size = len(arr)
    stack = []

    def backtrack(start, vol):
        if len(stack) == vol:
            results.append(stack.copy())
            return
        for i in range(start, size):
            stack.append(arr[i])
            backtrack(i + 1, vol)
            stack.pop()

    for v in range(size):
        backtrack(0, v)
    return results









def solution2(arr):
    results = []
    stack = []
    size = len(arr)

    def backtrack(start, vol):
        if len(stack) == vol:
            results.append(stack.copy())
            return
        for i in range(start, size):
            stack.append(arr[i])
            backtrack(i+1, vol)
            stack.pop()

    for v in range(size+1):
        backtrack(0, v)
    return results

if __name__ == '__main__':
    pprint(solution2([1,2,3,4]))
    # so = Solution()
    # res = so.subsets([1, 2, 3, 4])
    # pprint(res)
