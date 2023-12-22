import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = []

for _ in range(N):
    table.append(int(input()))

left, right = 1, max(table) * M

answer = 0
while left < right:
    answer = 0
    mid = (left + right) // 2

    for i in table:
        answer += mid // i

    if answer < M:
        left = mid + 1
    else:
        right = mid

print(right)