N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, max(nums),


def isValid(mid):
    low = nums[0]
    high = nums[0]
    count = 1

    for i in nums:
        if high < i:
            high = i

        if low > i:
            low = i

        if high - low > mid:
            count += 1
            low = i
            high = i

    return M >= count


answer = right
while left <= right:

    mid = (left + right) // 2

    if isValid(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)