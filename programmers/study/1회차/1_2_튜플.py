def solution(s):

    # 집합 문자열의 리스트로 변경 후 길이 짧은 순으로 정렬
    arr = list(sorted(s.replace('{', '').replace('},', ' ').replace('}', '').split(), key=lambda x:len(x)))
    print(arr)
    # 리스트의 각 요소 출력
    for i in range(len(arr)):
        arr[i] = list(int(a) for a in arr[i].split(','))

    print(arr)

    # 다음 요소에 있는 값을 모두 제거하기
    for i in range(len(arr) - 1, 0, -1):
        tmp = [j for j in arr[i] if j in arr[i - 1]]
        for t in tmp:
            arr[i].remove(t)

    answer = []
    for i in arr:
        answer.append(i[0])
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

# 백만 -> O(nlogn) or O(n)
# 공백 없이 { } , 로만 구성
# 튜플이 1개, 2개, 3개, 4개 순으로 나옴 (list 로 받아줘야 함)
