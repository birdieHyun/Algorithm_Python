from collections import deque

node, link = map(int, input().split())

visited = [False] * node

graph = [[] for _ in range(node + 1)]


def dfs(start, depth):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)


for _ in range(link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (1 + node)
count = 0

for i in range(1, node + 1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            dfs(i, 0)
            count +=1

print(count)
