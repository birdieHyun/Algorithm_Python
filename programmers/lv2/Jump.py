def solution(n):
    ans = 1

    while n != 1:
        if n % 2 == 0:
            n = int(n // 2)
        else:
            n = int(n // 2)
            ans += 1

    return ans