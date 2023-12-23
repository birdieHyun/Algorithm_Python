import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maps = [[] for _ in range(N + 1)]
weights = []

for _ in range(M):
    s_node, e_node, weight = map(int, input().split())
    weights.append(weight)
    maps[s_node].append([e_node, weight])
    maps[e_node].append([s_node, weight])

start_node, destination_node = map(int, input().split())

left = min(weights)
right = max(weights)


def bfs(start_weight):
    q = deque([start_node])
    visited = [False] * (N + 1)
    visited[start_node] = True

    while q:

        now = q.popleft()
        visited[now] = True

        for i in maps[now]:
            next_node = i[0]
            can_weight = i[1]

            if not visited[next_node] and can_weight >= start_weight:
                visited[next_node] = True
                q.append(next_node)

    if visited[destination_node]:
        return True
    return False


while left <= right:
    mid = (left + right) // 2
    can_move = bfs(mid)
    if can_move:
        left = mid + 1
    else:
        right = mid - 1

print(right)
