from collections import deque

N, M = map(int, input().split())
original_maps = [list(map(int, input().split())) for _ in range(N)]

# 바이러스 위치를 찾는다.
virus = deque()
for i in range(len(original_maps)):
    for j in range(len(original_maps[0])):
        if original_maps[i][j] == 2:
            virus.append((j, i))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(blocks):
    copy_map = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            copy_map[i][j] = original_maps[i][j]

    # 벽 3개를 세운다.
    for i in blocks:
        copy_map[i[1]][i[0]] = 1

    # 바이러스 시작하는 정점 삽입
    q = deque(virus)

    # visited 배열은 0 인 곳만 이동할 수 있게 할 것이기 때문에 만들지 않는다.

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

    # 안전 지대 카운트
    safety_zone = 0

    for i in range(N):
        safety_zone += copy_map[i].count(0)

    return safety_zone


blocks = deque()

answer = 0

# i / M = 세로 , i % M = 가로
for i in range(N * M - 2):
    if original_maps[int(i / M)][i % M] != 0:
        continue
    blocks.append((i % M, int(i / M)))
    for j in range(i + 1, N * M - 1):
        if original_maps[int(j / M)][j % M] != 0:
            continue
        blocks.append((j % M, int(j / M)))
        for k in range(j + 1, N * M):
            if original_maps[int(k / M)][k % M] != 0:
                continue
            blocks.append((k % M, int(k / M)))
            answer = max(bfs(blocks), answer)
            blocks.pop()
        blocks.pop()
    blocks.pop()

print(answer)
