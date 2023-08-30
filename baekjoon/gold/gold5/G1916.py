import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

node = int(input())
link = int(input())

graph = [[] for _ in range(node + 1)]

distance = [INF] * (node + 1)

for _ in range(link):
    # a 에서 b 로 가는데 c 만큼의 비용 소모
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 이미 방문한 노드는 건너뜀
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

print(distance[end])