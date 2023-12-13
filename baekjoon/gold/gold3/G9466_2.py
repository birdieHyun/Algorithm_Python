import sys

sys.setrecursionlimit(100000000)


def dfs(node):
    global result
    visited[node] = True
    cycle.append(node)
    next = std[node - 1]

    if visited[next]:
        if next in cycle:
            result += cycle[cycle.index(next) :]
            print(result)
        return
    else:
        dfs(next)


T = int(input())

for _ in range(T):

    n = int(input())
    std = list(map(int, input().split()))

    result = []
    visited = [False] * (n + 1)

    for i in range(n):
        if not visited[i + 1]:
            cycle = []
            dfs(i + 1)

    print(n - len(result))

