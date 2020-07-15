import sys


# 归并排序

def merge(a, b):
    i, j = 0, 0
    res = []
    while i < len(a) or j < len(b):
        if i == len(a):
            res.append(b[j])
            j += 1
            continue
        elif j == len(b):
            res.append(a[i])
            i += 1
            continue
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    return res


def merge_v2(a, b):
    i, j = 0, 0
    res = []
    a.append(100000000000000)
    b.append(100000000000000)
    while i < len(a) - 1 or j < len(b) - 1:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    return res


def merge_sort(arr):
    size = len(arr)
    if size <= 1:  # base case
        return arr
    mid = size >> 1  # 或 size // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    res = []
    i, j = 0, 0
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    while i < len(left) - 1 or j < len(right) - 1:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res


if __name__ == '__main__':
    aa = [5, 8, 10]
    bb = [3, 7, 12]
    print(merge(aa, bb))
    print(merge_v2(aa, bb))
    array = [56, 78, 23, 90, 21, 4, 5, 73, 11, 234]
    print(merge_sort(array))
