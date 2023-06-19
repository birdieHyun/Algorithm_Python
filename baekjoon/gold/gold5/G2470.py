total_count = int(input())
waters = list(map(int, input().split()))
waters.sort()

first_index = 0
last_index = len(waters) - 1

answer = [waters[first_index], waters[last_index]]
sum = waters[first_index] + waters[last_index]

abs_num = abs(sum)

while first_index != last_index:

    sum = waters[first_index] + waters[last_index]

    if abs_num > abs(sum):
        answer = [waters[first_index], waters[last_index]]
        abs_num = abs(sum)
        if abs_num == 0:
            break

    if sum < 0:
        first_index += 1
    else:
        last_index -= 1

print(answer[0], answer[1])
