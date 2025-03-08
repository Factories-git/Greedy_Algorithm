import sys

sys.setrecursionlimit(10 ** 10)
s = input()

n, m = 1, len(s)
graph = [list(map(int, s))]


def dfs_1(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 2
        dfs_1(x - 1, y)
        dfs_1(x, y - 1)
        dfs_1(x + 1, y)
        dfs_1(x, y + 1)
        return True
    return False


def dfs_2(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 2
        dfs_2(x - 1, y)
        dfs_2(x, y - 1)
        dfs_2(x + 1, y)
        dfs_2(x, y + 1)
        return True
    return False


result = result2 = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            if dfs_1(i, j):
                result += 1
        elif graph[i][j] == 0:
            if dfs_2(i,j):
                result2 += 1
print(min(result,result2))
