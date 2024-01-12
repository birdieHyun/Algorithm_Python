import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dots = list(map(int, input().split()))

lines = []
for _ in range(M):
    a, b = map(int, input().split())
    lines.append((a, b))

dots.sort()


def find_max(dot):
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2

        if dots[mid] <= dot:
            left = mid + 1
        else:
            right = mid - 1

    return right


def find_mid(dot):
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2

        if dots[mid] < dot:
            left = mid + 1
        else:
            right = mid - 1

    return right + 1


for a, b in lines:
    print(find_max(b) - find_mid(a) + 1)
