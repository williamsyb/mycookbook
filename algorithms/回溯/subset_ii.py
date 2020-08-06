from typing import List
from pprint import pprint


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        size = len(nums)
        result = []
        stack = []

        def backtrack(start, k):
            if len(stack) == k:
                result.append(stack.copy())
                return
            last = None
            for i in range(start, size):
                if nums[i] != last:
                    stack.append(nums[i])
                    backtrack(i + 1, k)
                    last = stack.pop()
            return

        for v in range(size + 1):
            backtrack(0, v)
        return result


def solution(arr):
    size = len(arr)
    results = []
    stack = []

    def backtrack(start, vol):
        if len(stack) == vol:
            results.append(stack.copy())
            return
        last=None
        for i in range(start, size):
            if arr[i] != last:
                stack.append(arr[i])
                backtrack(i+1, vol)
                last = stack.pop()

    for v in range(size+1):
        backtrack(0, v)
    return results



if __name__ == '__main__':
    so = Solution()
    # res = so.subsetsWithDup([1, 1, 1, 2, 3, 4])
    res = solution([1, 1, 1, 2, 3, 4])
    pprint(res)
