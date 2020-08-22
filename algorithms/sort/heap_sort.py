"""
堆排序算法的步骤：
1. 把无序数组构建成二叉堆（最大堆）。
2. 循环删除堆顶元素，移到集合尾部，调节堆产生新的堆顶。
"""


def heap_sort(arr):
    # 1. 将无序数组构建成二叉堆
    build_heap(arr)
    # 2.循环删除堆顶元素，移到集合尾部，调节堆产生新的堆顶。
    for i in range(len(arr) - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        down_adjust(arr, 0, i)
    print('排序完毕：', arr)


def down_adjust(arr, parent_index, size):
    """
    将小的“父亲”结点下沉
    :param arr:
    :param parent_index:
    :param size:
    :return:
    """
    parent = arr[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < size:
        if child_index + 1 < size and arr[child_index + 1] > arr[child_index]:
            child_index += 1
        if parent > arr[child_index]:
            break
        arr[parent_index] = arr[child_index]
        parent_index = child_index
        child_index = 2 * child_index + 1
    arr[parent_index] = parent


def build_heap(arr):
    print('原始数组：', arr)
    for i in range((len(arr) - 2) // 2, -1, -1):
        down_adjust(arr, i, len(arr))
    print('最大堆构建完毕：', arr)


if __name__ == '__main__':
    heap_sort([6, 7, 9, 3, 5, 1, 78, 54, 23, 43, 56, 88])
