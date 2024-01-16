n = int(input())

maps = []
answer = []
visited = [False] * n
min_diff = int(10e9)

for _ in range(n):
    maps.append(list(map(int, input().split())))


def dfs(depth, idx):
    global min_diff

    if depth == n // 2:
        power1, power2 = 0, 0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += maps[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += maps[i][j]
        min_diff = min(min_diff, abs(power1 - power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

dfs(0, 0)
print(min_diff)