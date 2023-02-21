INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 인접 리스트 방식 예제
graph = [[] for _ in range(3)]

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 2에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0, 7))

print(graph)
