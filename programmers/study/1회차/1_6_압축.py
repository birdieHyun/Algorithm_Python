def solution(msg):
    msg = msg.upper()
    answer = []
    index = dict()
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(1, len(alpha) + 1, 1):
        index[alpha[i - 1]] = i

    start, end = 0, 1
    while end < len(msg) + 1:
        s = msg[start:end]
        if s in index:
            end += 1
        else:
            answer.append(index[s[:-1]])
            index[s] = len(index) + 1
            start = end - 1
    answer.append(index[s])
    return answer

solution('KAKAO')

# msg 길이는 1000
# 미리 A ~ Z 까지 색인 등록해놓음
# 현재 글자부터 다음 글자까지 색인 안될때까지 찾음
# 만약 없으면 색인 추가하고 출력
