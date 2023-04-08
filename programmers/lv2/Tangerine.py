from collections import Counter
def solution(k, tangerine):
    answer = 0

    # 귤의 개수로 정렬
    count = sorted(Counter(tangerine).items(), reverse=True, key=lambda x: x[1])

    # 귤의 개수가 0까지 종류 count
    for key, value in count:
        if k <= 0:
            break
        k -= value
        answer += 1

    return answer

k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

print(solution(k, tangerine))
