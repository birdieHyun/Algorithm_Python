nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
answer = []


for i in range(len(nums) - 2):
    left = i + 1
    right = len(nums) - 1
    while left < right:
        now = nums[i]

        three_sum = now + nums[left] + nums[right]

        if three_sum == 0:
            answer.append([now, nums[left], nums[right]])
            break
        elif three_sum < 0:
            left += 1
        else:
            right -= 1

print(answer)
