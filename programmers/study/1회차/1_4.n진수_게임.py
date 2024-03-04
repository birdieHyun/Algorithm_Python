def convert(num, base):
    temp = "0123456789ABCDEF" # 16진수까지 있으므로
    q, r =divmod(num, base) # divmod 는 몫과 나머지를 return 함

    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]

def solution(n, t, m, p):
    answer = ''
    test = ''
    for i in range(m * t):
        test += str(convert(i, n))

    while len(answer) < t:
        answer += test[p - 1]
        p += m

    return answer


# 2진법부터 16진법까지 = n
# 미리 구할 숫자 t 는 1000 개
# 게임에 참가하는 인원 m 은 2인부터 100인까지
# 튜브의 순서는 p
# 1000개의 수를 진법으로 계산해서 list 적어두고 p 순서 + m 대로 찾으면 안됨?