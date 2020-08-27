"""
字节跳动笔试题

也是leetcode第42题：接雨水

"""


def solution(arr):
    res = 0
    for i in range(1, len(arr) - 1):
        left_max = max(arr[:i])
        right_max = max(arr[i + 1:])
        min_val = min(left_max, right_max)
        if min_val <= arr[i]:
            continue
        else:
            res += min_val - arr[i]
    return res


if __name__ == "__main__":
    print(solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
