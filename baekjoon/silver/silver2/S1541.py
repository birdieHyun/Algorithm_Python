import re

answer = 0
nums = str(input())
tmp = 0
num_list = re.split('(\+|-)', nums)

for i in range(len(num_list) - 1, -1, -2):
    tmp += int(num_list[i])
    if num_list[i - 1] == '+':
        continue
    if num_list[i - 1] == '-':
        tmp *= -1
        answer += tmp
        tmp = 0
        continue

    answer += tmp

print(answer)