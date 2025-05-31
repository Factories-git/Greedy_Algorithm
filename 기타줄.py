n, m = map(int, input().split())
package = [list(map(int, input().split())) for i in range(m)]
pack_1 = sorted(package)
pack_2 = sorted(package, key=lambda x:x[1])

v1 = pack_1[0][0] * (n // 6 + 1) if n % 6 != 0 else pack_1[0][0] * (n // 6)
v2 = pack_1[0][0] * (n // 6) + pack_2[0][1] * (n % 6)
v3 = pack_2[0][1] * n
print(min(v1, v2, v3))