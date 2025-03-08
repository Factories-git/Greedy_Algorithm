time = int(input())
times = [300,60,10]
l = []
for i in times:
    count = time // i
    time -= count * i
    l.append(count)
if time == 0:
    for i in l:
        print(i, end=' ')
else:
    print(-1)