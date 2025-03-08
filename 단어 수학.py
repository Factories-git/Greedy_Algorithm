n = int(input())
words = [input() for i in range(n)]

c = {}
for word in words:
    l = len(word)
    for i in range(l):
        ch = word[i]
        if ch not in c:
            c[ch] = 0
        c[ch] += 10 ** (l - i - 1)

sorted_c = sorted(c.items(), key=lambda x: -x[1])
digit = 9
words_to_letter = {}
for alpha, _ in sorted_c:
    words_to_letter[alpha] = digit
    digit -= 1

total_sum = 0
for word in words:
    number = 0
    for char in word:
        number = number * 10 + words_to_letter[char]
    total_sum += number
print(total_sum)