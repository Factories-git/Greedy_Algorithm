import sys

n = int(input())
positive_arr = []
negative_arr = []
for i in range(n):
    num = int(input())
    if num > 0:
        positive_arr.append(num)
    else:
        negative_arr.append(num)

positive_arr.sort(reverse=True)
negative_arr.sort()
re = 0
positive_visited = [False] * len(positive_arr)
negative_visited = [False] * len(negative_arr)

for i in range(len(positive_arr)-1):
    if positive_visited[i]:
        continue
    if positive_arr[i] + positive_arr[i+1] < positive_arr[i] * positive_arr[i+1]:
        re += positive_arr[i] * positive_arr[i+1]
        positive_visited[i+1] = True
    else:
        re += positive_arr[i]
if positive_arr:
    if not positive_visited[-1]:
        re += positive_arr[-1]

for i in range(len(negative_arr)-1):
    if negative_visited[i]:
        continue
    if negative_arr[i] + negative_arr[i+1] < negative_arr[i] * negative_arr[i+1]:
        re += negative_arr[i] * negative_arr[i+1]
        negative_visited[i+1] = True
    else:
        re += negative_arr[i]
if negative_arr:
    if not negative_visited[-1]:
        re += negative_arr[-1]
print(re)
