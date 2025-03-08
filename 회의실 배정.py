import sys

input = sys.stdin.readline
n = int(input())
times = []
for i in range(n):
    start,end = map(int, input().split())
    times.append([start,end])
times.sort(key=lambda x : x[0])
times.sort(key=lambda x : x[1])

cnt = 1
finish = times[0][1]
for i in range(1,n):
    if times[i][0] >= finish:
        cnt += 1
        finish = times[i][1]
print(cnt)