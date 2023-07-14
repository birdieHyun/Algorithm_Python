import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

test_case = int(input())


def dijkstra(student, start):
    q = []
    heapq.heappush(q, (0, start))
    distance[student][start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[student][now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[student][i[0]]:
                distance[student][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


for test_order in range(1, test_case + 1):
    answer = 0
    students, relations = map(int, input().split())
    graph = [[] for _ in range(students + 1)]
    distance = [[INF] * (students + 1) for _ in range(students + 1)]

    for _ in range(relations):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    for i in range(1, students + 1):
        dijkstra(i, i)

    print('#' + str(test_order), answer)

print(distance)
