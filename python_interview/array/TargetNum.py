nums = [2, 7, 11, 15]
target = 9

def find_target(numbers, target_num):

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_num:
                return [i, j]

print(find_target(nums, target))

# 투 포인터 이용 -> 그러나 이렇게 되면 인덱스가 섞여버리기 때문에 좋은 방법은 아니다. 투포인터는 정렬된 상황에서 사용하도록 하자

def find_target2(numbers, target_num):
    first, last = 0, len(numbers) - 1
    while first < last:
        if numbers[first] + numbers[last] == target_num:
            return [first, last]
        elif numbers[first] + numbers[last] > target_num :
            last -= 1
        else:
            first += 1

print(find_target2(nums, target))

