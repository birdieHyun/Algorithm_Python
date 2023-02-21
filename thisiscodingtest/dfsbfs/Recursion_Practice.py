def recursion(i):
    if i == 100:
        return
    print(i, '번째 함수에서 ', i + 1, '번째 함수를 호출합니다')
    recursion(i + 1)
    print(i, '번째 함수를 종료합니다')


recursion(1)


# 두 가지 방식으로 구현한 팩토리얼 예제

def factorial_1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial_1(5))


def factorial_2(n):
    if n <= 1:
        return 1
    return n * factorial_2(n - 1)


print(factorial_2(5))
