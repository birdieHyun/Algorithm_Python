import heapq
import sys

input = sys.stdin.readline

INF = int(10e9)
N, E = map(int, input().split())

distance = [INF] * (N + 1)
distance2 = [INF] * (N + 1)
distance3 = [INF] * (N + 1)

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

first_node, second_node = map(int, input().split())


def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0],))

if E == 0 or first_node > N or second_node > N or first_node < 1 or second_node < 1:
    answer = -1
else:
    dijkstra(1, distance)
    dijkstra(first_node, distance2)
    dijkstra(second_node, distance3)

    answer1 = distance[first_node] + distance2[second_node] + distance3[N]
    answer2 = distance[second_node] + distance3[first_node] + distance2[N]

    answer = min(answer1, answer2)

    if answer == INF:
        answer = -1
print(answer)
