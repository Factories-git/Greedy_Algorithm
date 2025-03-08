answer = 0
a = list(map(str, input().split('-')))


def my_sum(string):
    re = 0
    string = string.split('+')
    for i_ in string:
        re += int(i_)
    return re


for i in range(len(a)):
    s = my_sum(a[i])
    if i == 0:
        answer += s
    else:
        answer -= s

print(answer)