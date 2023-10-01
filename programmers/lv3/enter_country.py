def solution(n, times):
    MAX = 1_000_000_000
    left = 1
    right = MAX * MAX

    while left < right:
        mid = (right + left) // 2
        if (possible(n, times, mid)):
            right = mid
        else:
            left = mid + 1

    return left

def possible(n, times, mid):
    for i in times:
        n -= mid // i

    return n <= 0

n = 6
times = [7, 10]

print(solution(n, times))