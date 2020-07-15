from copy import deepcopy


def quick_sort(li):
    if not li:
        return []
    li = deepcopy(li)

    bm = li[0]
    more = [item for item in li if item > bm]
    less = [item for item in li if item < bm]
    return quick_sort(less) + [bm] + quick_sort(more)


if __name__ == '__main__':
    arr = [56, 78, 23, 90, 21, 4, 5, 73, 11, 234]
    print(quick_sort(arr))
