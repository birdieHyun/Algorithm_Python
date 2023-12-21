n, needs = map(int, input().split())
lan = []
for _ in range(n):
    lan.append(int(input()))

left, right = 0, max(lan)

while left <= right:
    total = 0
    mid = (left + right) // 2
    if mid == 0:
        break
    for i in lan:
        total += i // mid

    if total >= needs:
        left = mid + 1
    else:
        right = mid - 1

print(right)