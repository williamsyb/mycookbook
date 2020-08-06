
def solution(arr):
    size = len(arr)
    results = []
    stack = []
    flags = [False] * size

    def backtrack(start):
        if len(stack) == size:
            results.append(stack.copy)
            return

        for i in range(size):
            if not flags[i]:
                stack.append(arr[i])
                flags[i]=True


    for i in range(size):
        flags[i] = True
        backtrack(i)
        flags = [False] * size