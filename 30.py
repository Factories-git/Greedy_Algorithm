n = input()

if '0' not in n:
    print(-1)
    exit()

s = 0
for i in str(n):
    s += int(i)
if s % 3 != 0:
    print(-1)
    exit()
print(''.join(sorted(n, reverse=True)))