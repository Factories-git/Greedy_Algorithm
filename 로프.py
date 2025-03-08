import sys

input = sys.stdin.readline

n = int(input())
ropes = sorted([int(input()) for _ in range(n)], reverse=True)
val = 0
for i in range(n):
    if val < ropes[i] * (i+1):
        val = ropes[i] * (i+1)
print(val)