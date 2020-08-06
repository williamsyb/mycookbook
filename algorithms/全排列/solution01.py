from pprint import pprint


def permutations(arr, position, end, result):
    if position == end:
        # print(arr)
        result.append(arr.copy())

    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end, result)
            arr[index], arr[position] = arr[position], arr[index]


def solution(li):
    size = len(li)
    results = []
    stack = []
    def permutations2(position, end):
        if len(stack) == size:
            results.append(stack.copy())
            return
        for index in range(position, end):
            stack.append(li[index])
            permutations2(index+1, size)
            stack.pop()

    for i in range(size):
        permutations2(i, size, )
    return results


if __name__ == '__main__':
    arr1 = ["a", "b", "c"]
    # res = []
    # permutations(arr1, 0, len(arr1), res)
    # pprint(res)
    pprint(solution(arr1))
