import sys

sys.setrecursionlimit(1000000)

def dfs(node):
    global result
    visited[node] = True
    cycle.append(node)
    number = std[node - 1]

    if visited[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number)

T = int(input())

for _ in range(T):

    N = int(input())
    std = list(map(int, input().split()))
    visited = [False] * (N + 1)
    result = []

    for i in range(N):
        if not visited[i + 1]:
            cycle = []
            dfs(i + 1)

    print(N - len(result))
