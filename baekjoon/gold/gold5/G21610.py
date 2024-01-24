n, m = map(int, input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

moves = []
for _ in range(m):
    moves.append(list(map(int, input().split())))


# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx8 = ['empty', -1, -1, 0, 1, 1, 1, 0, -1]
dy8 = ['empty', 0, -1, -1, -1, 0, 1, 1, 1]

# 대각 4방향
dx4 = [-1, 1, -1, 1]
dy4 = [-1, -1, 1, 1]

clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

# 최대 100
for direction, distance in moves:
    moved_cloud = []

    for y, x in clouds:
        # 구름 위치 이동
        nx = (x + dx8[direction] * distance) % n
        ny = (y + dy8[direction] * distance) % n

        # 위치에 물 추가
        maps[ny][nx] += 1
        # 움직인 구름 위치 표기
        moved_cloud.append((ny, nx))

    for y, x in moved_cloud:
        # 이동한 구름의 대각 4방향 조사
        count = 0

        for i in range(4):
            nx = x + dx4[i]
            ny = y + dy4[i]

            # 경계 벗어나면 continue
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if maps[ny][nx] > 0:
                count += 1

        maps[y][x] += count

    new_clouds = []

    for i in range(n):
        for j in range(n):
            # 이동한 구름의 좌표와 동일하지 않고, 물의 양이 2 이상인 경우
            if (i, j) in moved_cloud or maps[i][j] < 2:
                continue

            # 물을 2만큼 빼고, 새로운 구름 추가
            maps[i][j] -= 2
            new_clouds.append((i, j))
    clouds = new_clouds

answer = 0

for i in range(n):
    for j in range(n):
        answer += maps[i][j]

print(answer)
