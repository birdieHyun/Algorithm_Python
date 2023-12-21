n = int(input())
budget = list(map(int, input().split()))
max_b = int(input())


left = 0
right = max(budget)

answer = 0

while left <= right:
    ideal = 0
    mid = (left + right) // 2

    for i in budget:
        if i < mid:
            ideal += i
        else:
            ideal += mid

    if ideal <= max_b:
        left = mid + 1
    else:
        right = mid - 1


print(right)
