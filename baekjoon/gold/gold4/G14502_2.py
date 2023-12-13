# N M = 최대 8 * 8
# 벽 3개를 세울 수 있는 최대 경우의 수 = 64 * 63 * 63 = 250,000
# 25만개의 경우의 수를 bfs 돌린다면 250,000 * 64 = 16,000,000 (천육백만)
# -> 완탐 해도 시간 가능
from collections import deque


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

virus = deque()
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            virus.append((j, i))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(walls):
    copy_map = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            copy_map[i][j] = maps[i][j]

    for i in walls:
        copy_map[i[1]][i[0]] = 1

    q = deque(virus)

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if copy_map[ny][nx] == 1:
                continue

            if copy_map[ny][nx] == 0:
                copy_map[ny][nx] = 2
                q.append((nx, ny))

    # 안전지대 확인
    safety = 0

    for i in copy_map:
        safety += i.count(0)

    return safety

answer = 0
walls = deque()

for i in range(N * M - 2):
    if maps[int(i / M)][i % M] != 0:
        continue
    walls.append((i % M, int(i / M)))
    for j in range(i + 1, N * M - 1):
        if maps[int(j / M)][j % M] != 0:
            continue
        walls.append((j % M, int(j / M)))
        for k in range(j + 1, N * M):
            if maps[int(k / M)][k % M] != 0:
                continue
            walls.append((k % M, int(k / M)))
            answer = max(bfs(walls), answer)
            walls.pop()
        walls.pop()
    walls.pop()

print(answer)
