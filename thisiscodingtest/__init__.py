# def solution(s, N):
#     # 1부터 N까지의 숫자를 문자열로 변환하여 집합으로 저장
#     digits_set = set(str(i) for i in range(1, N+1))
#
#     # 결과를 저장할 리스트
#     results = []
#
#     # 문자열을 순회하면서 각 부분 문자열에 대해 검사
#     for i in range(len(s) - N + 1):
#         # 현재 부분 문자열
#         substring = s[i:i+N]
#
#         # 부분 문자열의 각 숫자를 집합으로 변환
#         substring_set = set(substring)
#
#         # 부분 문자열이 원하는 조건을 만족하는지 검사
#         if substring_set == digits_set:
#             # 조건을 만족하면 결과 리스트에 추가
#             results.append(substring)
#
#     if not results:
#         return -1
#
#     return int(max(results))
#
# s = '12345321'
# N = 3
#
# answer = solution(s, N)
# print(answer)

##############
from collections import deque, defaultdict

def solution(relationships, target, limit):
    graph = defaultdict(set)
    for a, b in relationships:
        graph[a].add(b)
        graph[b].add(a)

    level = {target: 0}  # 노드의 레벨을 저장
    queue = deque([target])
    known_friends = set()  # 알고 있는 친구들
    new_friends = set()  # 새롭게 알게 된 친구들

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in level:  # 아직 방문하지 않은 노드
                level[neighbor] = level[node] + 1
                if level[neighbor] == 1:
                    known_friends.add(neighbor)
                elif level[neighbor] <= limit:
                    new_friends.add(neighbor)
                queue.append(neighbor)

    return len(known_friends) * 5 + len(new_friends) * 10 + len(new_friends)


###################
import re


def find_representative_names(names):
    pattern = re.compile(r'[&().,-]')
    special_max_names = []
    max_len = 0

    for name in names:
        name_len = len(name.replace(" ", ""))
        if pattern.search(name):
            special_max_names.append(name)
        elif name_len > max_len:
            max_len = name_len
            special_max_names = [name]
        elif name_len == max_len:
            special_max_names.append(name)

    return special_max_names


names = [
    "토스커피사일로&베이커리",
    "토스커피사일로 베이커리",
    "토스커피사일로 베이커",
    "토스커피사일로 베이",
    "토스커피사일",
    "비바리퍼블리카 식당",
    "비바리퍼블리카식",
    "비바리퍼블리"
]

special_max_names = find_representative_names(names)
print(special_max_names)  # 출력: ['토스커피사일로&베이커리', '비바리퍼블리카 식당']
