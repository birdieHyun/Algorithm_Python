rice_count, rice_length = map(int, input().split())

rice_list = list(map(int, input().split()))

start = 0
end = max(rice_list)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in rice_list:
        if x > mid:
            total += x - mid

    if total < rice_length:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

