import sys, heapq

input = sys.stdin.readline

n = int(input())

time = [list(map(int, input().split())) for i in range(n)]

time.sort()

teach = []

heapq.heappush(teach, time[0][1])
for i in range(1, n):
    if time[i][0] < teach[0]:
        heapq.heappush(teach, time[i][1])
    else:
        heapq.heappop(teach)
        heapq.heappush(teach, time[i][1])
print(len(teach))