import math


def solution(n):
    answer = 0

    for i in range(2, n + 1):
        if checkPrime(i) == True:
            answer += 1

    return answer


def checkPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


print(solution(5))

# 2/n 만큼 배수는 제외
