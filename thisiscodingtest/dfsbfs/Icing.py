from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        visited[v] = True
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * 20

graph = []
n, m = map(int, input().split())
for i in range(n):
    graph.append(list(map(int, input())))

bfs(graph, 1, visited)