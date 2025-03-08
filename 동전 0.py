cash = []
n,k = map(int, input().split())
now = k
re = 0
for i in range(n):
    cash.append(int(input()))
cash.sort(reverse=True)
for i in cash:
    if now - i >= 0:
        couny = now // i
        re += couny
        now -= couny * i
print(re)