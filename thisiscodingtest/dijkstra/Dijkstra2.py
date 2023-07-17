import heapq

INF = int(1e9)

# 노드의 개수 간선의 개수 입력받기
n, m = map(int, input().split())

# 시작점 입력받기
start = int(input())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)


# 그래프간 연결정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        # 탐색하지 않았더라면 연결된 노드들 탐색
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
























