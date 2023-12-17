from collections import deque
import sys

input = sys.stdin.readline

n, k, m = map(int, input().split())

visited = [False] * (n + 1)
cost = [0] * (n + 1)
cost[1] = 1

hyper_tube = []
nodes = [[] for _ in range(n + 1)]

# 노드들이 어느 하아퍼 튜브에 연결되어 있는지 저장
for i in range(m):
    tube = list(map(int, input().split()))
    for j in tube:
        nodes[j].append(i)
    hyper_tube.append(tube)

def bfs(node):
    q = deque()
    q.append(node)

    while q:
        now = q.popleft()
        visited[now] = True

        next_tube = nodes[now]

        for i in next_tube:
            for j in hyper_tube[i]:
                if not visited[j]:

                    print(j)
                    visited[j] = True
                    q.append(j)
                    cost[j] = cost[now] + 1


bfs(1)

answer = cost[n]
if cost[n] == 0:
    answer = -1
print(answer)

# 모든 간선을 연결할 경우 1000^3 메모리 사용 -> 메모리 초과

# 하이퍼튜브를 하나의 노드로 간주함
