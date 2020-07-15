from pprint import pprint


def permutations(arr, position, end, result):
    if position == end:
        # print(arr)
        result.append(arr)

    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end, result)
            arr[index], arr[position] = arr[position], arr[index]


if __name__ == '__main__':
    arr = ["a", "b", "c"]
    res = []
    permutations(arr, 0, len(arr), res)
    pprint(res)
