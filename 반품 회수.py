import sys
input = sys.stdin.readline

N = int(input())
X = [0, *map(int, input().split())]
T = [0, *map(int, input().split())]

res = 2 * X[N]
for i in range(1, N + 1):
    res = max(res, T[i] + X[i])

print(res)