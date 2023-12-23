import sys

input = sys.stdin.readline

N, C = map(int, input().split())

houses = []

for _ in range(N):
    houses.append(int(input()))

houses.sort()

left, right = 1, max(houses) - min(houses)


def checking(wifi_range):
    global count
    global answer

    answer_range = []
    start = 0

    for i in range(1, len(houses)):
        if houses[i] - houses[start] >= wifi_range:
            answer_range.append(houses[i] - houses[start])
            start = i
            count += 1

    if count >= C:
        answer = max(answer, min(answer_range))
        return True

    return False


answer = 0
count = 1
while left <= right:
    mid = (left + right) // 2

    count = 1

    bool = checking(mid)

    if bool:
        left = mid + 1
    else:
        right = mid - 1

print(answer)
