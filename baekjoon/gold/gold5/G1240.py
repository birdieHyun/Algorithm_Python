# N개의 노드로 이루어진 트리가 주어지고 M개의 두 노드 쌍을 입력받을 때 두 노드 사이의 거리를 출력하라.
# N, M < 1000
# 노드의 개수, 노드 쌍의 개수
from collections import deque


N, M = map(int, input().split())

links = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    x, y, v = map(int, input().split())

    # x 에서 y 까지 v 만큼 걸린다.
    links[x].append((y, v))
    links[y].append((x, v))


def bfs(start, target, move_cost):
    q = deque([start])
    move_cost[start] = 0
    visited = [False] * (N + 1)

    while q:
        now = q.popleft()
        visited[now] = True
        for i in links[now]:
            move_cost[i[0]] = min(move_cost[i[0]], move_cost[now] + i[1])
            if not visited[i[0]]:
                q.append(i[0])
        if now == target:
            print(move_cost[target])
            return

for _ in range(M):
    start, target = map(int, input().split())
    move_cost = [int(10e9)] * (N + 1)
    bfs(start, target, move_cost)

