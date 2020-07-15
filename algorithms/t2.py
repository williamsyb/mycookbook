def getSum(num):
    if num // 10 == 0:
        return num

    return num % 10 + getSum(num // 10)


# print(getSum(455))


def binsearch(arr, key, low, high):
    mid = (low + high) // 2
    print(f'low:{low}, high:{high}, mid:{mid}')
    if key == arr[mid]:
        return arr[mid]
    if low > high:
        return False
    if key < arr[mid]:
        return binsearch(arr, key, low, mid - 1)
    if key > arr[mid]:
        return binsearch(arr, key, mid + 1, high)


def binary_search_cur(arr, item):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == item:
            return True
        elif arr[mid] > item:
            return binary_search_cur(arr[:mid - 1], item)
        else:
            return binary_search_cur(arr[mid + 1:], item)


if __name__ == '__main__':
    array = [4, 13, 27, 38, 49, 49, 55, 65, 76, 97]
    ret = binsearch(array, 78, 0, len(array) - 1)
    print(ret)
    print(binary_search_cur(array, 760))
