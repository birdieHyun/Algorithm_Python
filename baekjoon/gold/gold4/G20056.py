n, m, k = map(int, input().split())

maps = [[] * (n + 1) for _ in range(n + 1)]
# r행 c열 질량 속력 방향
fires = []

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(m):
    fires.append(list(map(int, input().split())))

for _ in range(k):

    for fire in fires:
        y, x, mass, distance, direction = fire
        nx = (x + dx[direction] * distance) % n
        ny = (y + dy[direction] * distance) % n

        maps[ny][nx].append([mass, distance, direction])

        print(maps)
