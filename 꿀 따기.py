n = int(input()) #n 입력
honey = list(map(int, input().split())) #꿀 입력
max_l = [] #정답 리스트
sum_ = [] #구간합 리스트(매번 새로 구함)
#여기서 17번째 줄까지는 벌벌꿀 (벌이 왼쪽에 고정되어 있는 경우)
for i in range(1, n): #1부터 구하는 이유: 벌 하나는 맨 왼쪽에 고정시켜 놓아야 최적이기 때문.
    if sum_: #sum이 안 비어있다면
        sum_.append(honey[i] + sum_[-1]) #접두사 합 구하기
    else:
        sum_.append(honey[i]) #없으면 그냥 넣기
max_ = 0 #이 케이스에서의 최댓값 저장 변수
for i in range(1, n-1): #1부터 반복하는 이유 : 벌 하나는 맨 왼쪽에 고정시켜 놓았기 때문. n-1까지 하는 이유는 벌통 자리에 벌을 못 놓아서
    a = sum_[-1] - honey[i] #a는 맨 왼쪽 벌을 의미. 벌이 시작한 곳은 꿀을 딸 수 없어서 -1
    b = sum_[-1] - sum_[i - 1] # b는 움직이는 벌을 의미. 이 벌은 전의 것(전 인덱스) 까지는 못 먹으니 합의 top - 합의 i-1번째 만큼 먹을 수 있음.
    if max_ < a + b: #max 갱신 부분
        max_ = a + b
max_l.append(max_) #정답 변수에 추가

#여기서 32번째 줄 까지는 꿀벌벌 (벌 하나가 오른쪽에 고정된 경우)
sum_ = [] #새로운 구간합 구하기
for i in range(n - 2, -1, -1): # n-2 부터 시작하는 이유: 벌 하나는 오른쪽에 고정되어 있기 때문.
    if sum_: #여기부터는 상술한 것과 같음
        sum_.append(honey[i] + sum_[-1])
    else:
        sum_.append(honey[i])
max_ = 0
for i in range(n - 2, 0, -1): #벌을 오른쪽에 고정시켜 놓았기 때문에 , 1까지 하는 이유는 벌통 자리에 벌을 못 놓아서
    a = sum_[-1] - honey[i] # a는 맨 오른쪽 벌을 의미. 왜 인지는 위에서 설명.
    b = sum_[-1] - sum_[n-2-i] # b는 움직이는 벌을 의미. sum[-1] - sum[n-2-i]를 한 이유 : 위의 케이스와 똑같은데, 인덱스 장난질을 해야 하기 때문.
    if max_ < a + b: #max 갱신
        max_ = a + b
max_l.append(max_) #정답 변수에 넣기

sum_ = [0]
for i in range(1, n - 1): #구간합을 1부터 n-1까지 구하는 이유 : 가장자리에 벌을 놓았기 때문
    sum_.append(honey[i] + sum_[-1])
print(sum_)
max_ = 0
for i in range(1, n - 1): #여기도 반복을 이렇게 하는 이유 : 가장자리에 벌을 놓았기 때문
    a = sum_[i] #a는 맨 왼쪽 벌을 의미. 맨 왼쪽 벌은 방해 없이 벌통까지 먹을 수 있음
    b = sum_[- 1] - sum_[i - 1] #b는 맨 오른쪽 벌을 의미. 맨 오른쪽 벌은 마지막 - i-1 번째 까지만 먹을 수 있음. (벌통 까지 벌이 간다고 했으니)
    if max_ < a + b: #max 갱신
        max_ = a + b
max_l.append(max_)

print(max(max_l)) #세가지 경우 중, 최댓값 출력