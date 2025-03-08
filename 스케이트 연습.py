n = int(input())
speed = list(map(int, input().split()))
now = 0
re = 0
for i in speed[::-1]:
    if now < i:
        now += 1
    else:
        now = i
    re += now
print(re)