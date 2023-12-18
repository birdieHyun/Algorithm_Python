from collections import deque


def bfs(node, depth):
    global answer

    q = deque()
    q.append((node, depth))
    visited[node] = True

    while q:

        current_node, current_depth = q.popleft()

        for next_node in nodes[current_node]:
            if not visited[next_node] and current_depth <= 1:
                visited[next_node] = True
                q.append((next_node, current_depth + 1))
                answer += 1


n = int(input())
m = int(input())

visited = [False] * (n + 1)
nodes = [[] for _ in range(n + 1)]
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

bfs(1, 0)
print(answer)
