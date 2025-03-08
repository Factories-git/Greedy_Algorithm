import sys, heapq


input = sys.stdin.readline
n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])
hq = []

for d, c in arr:
    heapq.heappush(hq, c)
    if d < len(hq):
        heapq.heappop(hq)
print(sum(hq))