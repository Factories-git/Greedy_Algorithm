c = 0
n = int(input())
level = [int(input()) for _ in range(n)]
for i in range(n-2, -1, -1):
    if level[i+1] <= level[i]:
        c += level[i] - (level[i+1] - 1)
        level[i] = level[i+1] - 1
print(c)