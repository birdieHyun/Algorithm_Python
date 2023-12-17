from collections import deque


def bfs(node):
    q = deque([node])

    while q:
        next = q.popleft()

        if visited[next] == True:
            return False

        visited[next] = True

        nexts = nodes[next]
        for i in nexts:
            if not visited[i]:
                q.append(i)

    return True


count = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    answer = 0

    nodes = [[] for i in range(n + 1)]
    visited = [False] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)

    for i in range(1, n + 1):
        if not visited[i]:
            if bfs(i):
                answer += 1

    if answer == 0:
        print('Case', count, ': No trees.')
    if answer == 1:
        print('Case', count, ': There is one tree.')
    if answer > 1:
        print('Case', count, ': A forest of', answer, 'trees.')
    count += 1
