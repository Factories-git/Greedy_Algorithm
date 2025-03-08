import heapq
import sys

input = sys.stdin.readline


n,k = map(int, input().split())
gem = []
heap = []
heapq.heapify(heap)
re = 0
for i in range(n):
    kg,pri = map(int, input().split())
    gem.append([kg, pri])
back = [int(input()) for _ in range(k)]
gem.sort(reverse=True)
back.sort()
for b in back:
    while gem:
        w,v = gem.pop()
        if w > b:
            gem.append([w,v])
            break
        heapq.heappush(heap, [-v,w])

    if heap:
        v,w = heapq.heappop(heap)
        if w > b:
            heapq.heappush(heap, [v,w])
            continue
        re += -v
print(re)