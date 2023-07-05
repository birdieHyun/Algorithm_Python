nums = [2, 7, 11, 15]
target = 9

def find_target(numbers, target_num):

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_num:
                return [i, j]

print(find_target(nums, target))