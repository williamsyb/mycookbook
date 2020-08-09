from pprint import pprint
from typing import List

def solution(arr):
    size = len(arr)
    results = []
    stack = []
    flags = [False] * size

    def backtrack():
        if len(stack) == size:
            results.append(stack.copy())
            return

        for i in range(size):
            if not flags[i]:
                stack.append(arr[i])
                flags[i] = True
                backtrack()
                stack.pop()
                flags[i] = False

    backtrack()
    return results


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        route = []
        # cache_sum = 0
        total_sum = sum(nums)
        print(total_sum)
        def backtrack(t_sum, total_sum):

            if len(route) == len(nums) and t_sum == total_sum:
                results.append(route[:])
                return
            elif len(route) == len(nums) and t_sum != total_sum:
                return
            for item in nums:
                t_sum += item
                route.append(item)
                backtrack(t_sum,total_sum)
                t_sum -= route.pop()

        backtrack(0, total_sum)
        return results

if __name__ == '__main__':
    # pprint(solution([1, 2, 3, 4]))
    pprint(Solution2().permute([1, 2, 3, 4]))
