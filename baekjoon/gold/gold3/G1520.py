M, N = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(M)]
count = [[-1] * N for _ in range(M)]
count[M - 1][N - 1] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    if count[y][x] > -1:
        return count[y][x]

    count[y][x] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if maps[y][x] > maps[ny][nx]:
            count[y][x] += dfs(nx, ny)

    return count[y][x]


i = dfs(0, 0)
print(i)
