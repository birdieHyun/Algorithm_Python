import heapq

N, M = map(int, input().split())
# links = [list(map(int, input().split())) for _ in range(M)]
INF = int(10e9)

answer = []
links = []

def dijkstra(start, nodes):
    global links
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in nodes[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                links.append((now, i[0]))

                heapq.heappush(q, (cost, i[0],))

    return distance

nodes = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

# 하나씩 하는게 아닌, 최단경로에 해당하는 노드들의 연결을 하나씩 끊어봄
# for i in range(M):
#     distance = [INF] * (N + 1)
#     nodes = [[] for _ in range(N + 1)]
#     for j in range(len(links)):
#         if i == j:
#             continue
#
#         # 하나의 도로 없이 양방향 연결
#         start, end, value = links[j][0], links[j][1], links[j][2]
#         nodes[start].append((end, value))
#         nodes[end].append((start, value))
#
#     # 다익스트라로 최단거리 구하기
#     dijkstra(1, nodes)
#
#     answer.append(distance[N])
for i in range(M):
    a, b, c = map(int, input().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))


dijkstra(1,nodes)

print(links)
# print(answer)
# print(max(answer))

# 5 6
# 1 2 4
# 1 3 3
# 2 3 1
# 2 4 4
# 2 5 7
# 4 5 1
# [9, 9, 9, 11, 9, 11]

# 11
#
# 6 7
# 1 2 1
# 2 3 4
# 3 4 4
# 4 6 4
# 1 5 5
# 2 5 2
# 5 6 5
# [10, 8, 8, 8, 8, 10, 13]


# 13
