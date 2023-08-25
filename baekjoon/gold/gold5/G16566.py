# N * N 크기의 맵
# 0 빈칸, 1 집, 2 치킨집
# 치킨 거리 = | x - y | + | x - y |

# N 입력, 폐업시키지 않을 치킨집 M 입력
# 지도 입력

# 치킨집 어디 있는지 배열에 저장
# 치킨집 순열 생성
# 치킨집 순열 개수 만큼 for 문 전체 치킨맵 돌면서 집일 경우 치킨 거리 구하기
# 치킨 거리 배열에 저장한 다음 최소값 출력

import itertools

def chicken_dist(x, y, destination):
    answer = int(1e9)
    for i in destination:
        tmp = abs(x - i[0]) + abs(y - i[1])
        if tmp < answer:
            answer = tmp
    return answer


N, M = map(int, input().split())

chicken_map = [list(map(int, input().split())) for _ in range(N)]
chicken_list_tmp = []

for i in range(len(chicken_map)):
    for j in range(len(chicken_map[0])):
        if chicken_map[i][j] == 2:
            chicken_list_tmp.append([j, i])

chicken_list = list(itertools.combinations(chicken_list_tmp, M))

total_dist = []

for i in range(len(chicken_list)):
    each_dist = 0
    for y in range(N):
        for x in range(N):
            now = chicken_map[y][x]

            if now == 1:
                # 치킨 거리 구하는 함수
                each_dist += chicken_dist(x, y, chicken_list[i])
    total_dist.append(each_dist)

print(min(total_dist))