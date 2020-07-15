visit = [True, True, True]
temp = ["" for x in range(0, 3)]


def dfs(position):
    if position == len(arr):
        print(temp)
        return

    for index in range(0, len(arr)):
        if visit[index]:
            temp[position] = arr[index]
            visit[index] = False
            dfs(position + 1)
            visit[index] = True


arr = ["a", "b", "c"]

dfs(0)