from typing import List
from pprint import pprint

"""
LeetCode
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


def solution(arr, target):
    results = []
    stack = []
    size = len(arr)

    def backtrack(start, target):
        if target == 0:
            results.append(stack.copy())
            return
        if target < 0:
            return

        for i in range(start, size):
            stack.append(arr[i])
            target -= arr[i]
            backtrack(i, target)
            target += stack.pop()

    backtrack(0, target)
    return results


def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    n = len(candidates)
    result = []
    stack = []

    def backtrack(first=0, route_sum=0):

        if route_sum == target:
            result.append(stack.copy())
            return

        if route_sum > target:
            return

        for i in range(first, n):
            stack.append(candidates[i])
            route_sum += candidates[i]
            backtrack(i, route_sum)
            route_sum -= stack.pop()

        return

    backtrack()
    return result


class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []

        # 剪枝是为了提速，在本题非必需
        candidates.sort()
        # 在遍历的过程中记录路径，它是一个栈
        path = []
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy()
            res.append(path[:])
            return

        for index in range(begin, size):
            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            if residue < 0:
                break
            path.append(candidates[index])
            # 因为下一层不能比上一层还小，起始索引还从 index 开始
            self.__dfs(candidates, index, size, path, res, residue)
            path.pop()


if __name__ == '__main__':
    pprint(solution([2, 3, 6, 7], 7))
