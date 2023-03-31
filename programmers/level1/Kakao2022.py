# multi value set 만들어서 신고당한 회원(key) - 신고한 회원(value) 로 저장
from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)  # 0번 안내를 받는 것으로 초기화

    multi_map = defaultdict(set) # 하나의 키에 여러 value를 중복으로 받지 않는 map 생성

    for r in report:
        r = r.split()
        multi_map[r[1]].add(r[0])   # 신고당한 회원 (key) - 신고한 회원(value)

    for i in (multi_map):
        if len(multi_map[i]) >= k:     # 신고한 회원 >= k 일 경우 -> 신고한 회원의 알림 횟수 +1
            for person in multi_map[i]:
                index = id_list.index(person)
                answer[index] += 1


    return answer
