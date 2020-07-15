def selection_sort(li):
    size = len(li)
    for i in range(size - 1, 0, -1):
        max_loc = i
        for j in range(i):
            if li[j] > li[max_loc]:
                max_loc = j
        li[max_loc], li[i] = li[i], li[max_loc]
    return li


if __name__ == '__main__':
    arr = [56, 78, 23, 90, 21, 4, 5, 73, 11, 234]
    print('selection_sort:', selection_sort(arr))
