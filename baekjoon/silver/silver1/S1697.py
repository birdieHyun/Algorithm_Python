from collections import deque

def bfs(N):
    queue = deque()
    queue.append(N)
    while queue:
        tmp = queue.popleft()
        if tmp == K:
            return visited[K]
        for i in (tmp - 1, tmp + 1, tmp * 2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[tmp] + 1
                queue.append(i)


N, K = map(int, input().split())
visited = [0 for i in range(100001)]
print(bfs(N))