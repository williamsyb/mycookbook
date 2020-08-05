# -*- coding UTF-8 -*-
# @project : python03
# @Time    : 2020/7/7 10:21
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : triangle.py
# @Software: PyCharm
from functools import lru_cache

# 问题描述
"""
           2
        3     4
      6    5     7
    4   1     8    3
以上三角形由一连串的数字构成，要求从顶点 2 开始走到最底下边和的最小路径，
每次只能向当前节点下面的两个节点走，如 3 可以向 6 或 5 走，不能直接走到 7。


如:从 2 走到最底下最短路径为  2+3+5+1 = 11,即为我们所求的答案
"""


#  定义数据模型
triangle = [
    [2],
    [8, 4],
    [6, 5, 7, ],
    [9, 5, 4, 3, 5],
    [4, 1, 8, 2, 6, 3]
]


# @lru_cache()
# def traverse(i, j, total_row):
#     # total_row = 4
#     if i >= total_row - 1:
#         return 0
#     left_sum = traverse(i + 1, j, total_row) + triangle[i + 1][j]
#     right_sum = traverse(i + 1, j + 1, total_row) + +triangle[i + 1][j + 1]
#     return min(left_sum, right_sum)


class Solution:
    # 定义traverse_v2表示任一个结点(不妨设为i,j)的  ‘从该结点走起所计算出的<最小值>’，
    # 由于走法类似于二叉树，该节点(i,j)的traverse_v2计算值与其
    # 左右子结点的traverse_v2值的关系为
    # traverse_v2(i,j) - node(i,j)的值 = min( traverse_v2(i+1,j), traverse_v2(i+1,j+1) )
    # 此时考虑base case，判断出 当i的值达到了最后一层时，traverse_v2的值就是其node(i,j)本身的值

    # 递归的考虑出发点也可以从base case自底向上发散，有时候会更清晰，比如全排列
    @classmethod
    @lru_cache()
    def traverse_v2(cls, i, j, size):
        if i >= size - 1:  # 其实这里用 == 也是可以的
            return triangle[i][j]
        left = Solution.traverse_v2(i + 1, j, size)
        right = Solution.traverse_v2(i + 1, j + 1, size)
        res = max(left, right) + triangle[i][j]
        return res


if __name__ == '__main__':
    size_ = len(triangle)
    print(Solution.traverse_v2(0, 0, size_))
    # print(size)
    # res = traverse(0, 0, size) + triangle[0][0]
    # print(res)
