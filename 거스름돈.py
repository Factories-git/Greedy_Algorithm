money = 1000 - int(input())
cashs = [500,100,10,5,1]
count = 0
for i in cashs:
    if money % i == 0:
        count += 1
        money //= i
        print(i,count,money)
print(count)