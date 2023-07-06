from itertools import combinations

N, M = map(int, input().split())
answer = 0
home = []
chicken = []

chicken_map = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if chicken_map[i][j] == 1:
            home.append([i, j])
        if chicken_map[i][j] == 2:
            chicken.append([i, j])

# M 개 만큼의 치킨집을 남긴다
rand_chicken = list(combinations(chicken, M))
# 집과 치킨집의 거리 구한다.


