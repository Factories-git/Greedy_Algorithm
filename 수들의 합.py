n = int(input())
add = 0
i = 1
while True:
    add += i
    if add > n:
        print(i - 1)
        break
    i += 1