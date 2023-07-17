import heapq

INF = int(1e9)

# 노드와 간선의 개수
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

dis_x = [INF] * (n + 1)
dis_k = [INF] * (n + 1)

def dijkstra(start, distance):
    q = []

    heapq.heappush(q,(0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

answer_x = dijkstra(1, dis_x)
answer_k = dijkstra(x, dis_k)

print(answer_x)
print(answer_k)

print(answer_x[x], answer_k[k])
