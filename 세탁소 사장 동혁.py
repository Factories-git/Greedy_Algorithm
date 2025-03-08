for i in range(int(input())):
    j = int(input())
    q = j // 25
    j %= 25
    d = j // 10
    j %= 10
    n = j // 5
    j %= 5
    p = j // 1
    j %= 1

    print(q,d,n,p)