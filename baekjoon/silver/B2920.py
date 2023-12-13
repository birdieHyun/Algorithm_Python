nums = list(map(int, input().split()))

answer = ''
if nums[0] > nums[1]:
    answer = 'descending'
else:
    answer = 'ascending'

for i in range(2, len(nums)):
    if nums[i - 1] > nums[i]:
        tmp = 'descending'
        if tmp != answer:
            answer = 'mixed'
            break

    elif nums[i - 1] < nums[i]:
        tmp = 'ascending'
        if tmp != answer:
            answer = 'mixed'
            break

print(answer)
