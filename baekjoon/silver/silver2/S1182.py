from itertools import combinations

numbers, total = map(int, input().split())

number_list = list(map(int, input().split()))

answer = 0

for i in range(1, len(number_list) + 1):
    for j in combinations(number_list, i):
        if sum(j) == total:
            answer += 1

print(answer)