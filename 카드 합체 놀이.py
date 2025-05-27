import heapq

n, c = map(int, input().split())
arr = list(map(int, input().split()))
heapq.heapify(arr)

for i in range(c):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    re = a + b
    heapq.heappush(arr ,re)
    heapq.heappush(arr ,re)
print(sum(arr))