def convert(n, q) : # n진수 변환 함수
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]

def getPrimeNum(n): # 소수 찾기 함수
    if n == 1 :
        return False
    elif n == 2 :
        return True
    m = int(n ** 0.5) + 1
    for i in range(2, m):
        if n % i == 0 :
            return False
    return True

def solution(n, k): # K진수에서 소수 개수 구하기 함수
    n = convert(n, k)
    lists = str(n).split('0')
    lists = list(filter(lambda x: x != '', lists))
    lists = list(map(lambda x: getPrimeNum(int(x)), lists))
    return lists.count(True)

# 양의 정수 n
# 진수 k
# O(n) or O(n log n)

# 주어진 N 을 K 진수로 바꾸기
# 소수인지 판별하기