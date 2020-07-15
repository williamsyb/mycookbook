def bubble_sort(li):
    size = len(li)
    for i in range(size - 1, 0, -1):
        for j in range(i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li


if __name__ == '__main__':
    arr = [56, 78, 23, 90, 21, 4, 5, 73, 11, 234]
    print(bubble_sort(arr))
