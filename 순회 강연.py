import heapq

heap = []
day = []
heapq.heapify(heap)
for i in range(int(input())):
    p, d = map(int, input().split())
    day.append(d)
    heapq.heappush(heap, (-p, d))
print(heap)
finish = [False] * max(day)
money = 0
while heap:
    p, d = heapq.heappop(heap)
    if not finish[d-1]:
        money += -p
        finish[d-1] = True
print(money)