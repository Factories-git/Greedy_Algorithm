n = int(input())
weight = sorted(map(int, input().split()))

tar = 1
for w in weight:
    if tar < w:
        break
    tar += w
print(tar)
