n = int(input())
honey = list(map(int, input().split()))
max_l = []
sum_ = []
for i in range(1, len(honey)):
    if sum_:
        sum_.append(honey[i] + sum_[-1])
    else:
        sum_.append(honey[i])
max_ = 0
for i in range(1, len(honey)-1):
    a = sum_[-1] - honey[i]
    b = sum_[-1] - sum_[i - 1]
    if max_ < a + b:
        max_ = a + b
max_l.append(max_)

sum_ = []
for i in range(len(honey) - 2, -1, -1):
    if sum_:
        sum_.append(honey[i] + sum_[-1])
    else:
        sum_.append(honey[i])
max_ = 0
for i in range(len(honey) - 2, 0, -1):
    a = sum_[-1] - honey[i]
    b = sum_[-1] - sum_[len(honey)-2-i]
    if max_ < a + b:
        max_ = a + b

max_l.append(max_)
sum_ = [0]
for i in range(1, len(honey) - 1):
    if sum_:
        sum_.append(honey[i] + sum_[-1])
    else:
        sum_.append(honey[i])
max_ = 0
for i in range(1, len(honey) - 1):
    a = sum_[i]
    b = sum_[- 1] - sum_[i - 1]
    if max_ < a + b:
        max_ = a + b
max_l.append(max_)

print(max(max_l))