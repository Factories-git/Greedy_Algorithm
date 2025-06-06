def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    left = 0
    right = len(people)-1
    while left <= right:
        if people[left] + people[right] > limit:
            answer += 1
            left += 1
        else:
            answer += 1
            right -= 1
            left += 1
    return answer


print(solution([150, 120, 80, 80, 70, 40], 150))