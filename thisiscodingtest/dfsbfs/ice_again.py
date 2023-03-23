height, width = map(int, input().split())

graph = []

for i in range(height):
    graph.append(list(map(int, input())))

answer = 0


def dfs(x, y):
    if x <= -1 or x >= height or y <= -1 or y >= width:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x - 1, y)
        return True
    return False


for i in range(height):
    for j in range(width):
        if dfs(i, j) == True:
            answer += 1

print(answer)
