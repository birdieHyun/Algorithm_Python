from collections import deque
import sys

input = sys.stdin.readline

node, link, start = map(int, input().split())

dfs_visited = [False] * (node + 1)
bfs_visited = [False] * (node + 1)

map_link = [[] for _ in range(node + 1)]

for _ in range(link):
    a, b = map(int, input().split())
    map_link[a].append(b)
    map_link[b].append(a)

for i in map_link:
    i.sort()

def dfs(start):
    dfs_visited[start] = True
    print(start, end=' ')
    for i in map_link[start]:
        if not dfs_visited[i]:
            dfs(i)

def bfs(start):
    bfs_visited[start] = True
    q = deque()
    q.append(start)

    while q:
        next_node = q.popleft()
        print(next_node, end=' ')

        for i in map_link[next_node]:
            if not bfs_visited[i]:
                bfs_visited[i] = True
                q.append(i)

dfs(start)
print()
bfs(start)