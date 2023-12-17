k = int(input())
import sys

sys.setrecursionlimit(1000000000)
input = sys.stdin.readline


def dfs(node):
    global answer
    if color[node] == 0:
        color[node] = 1
    next = maps[node]

    for i in next:
        if node == i:
            answer = 'NO'
            return

        if color[i] != 0 and color[node] == color[i]:
            answer = 'NO'
            return

        if color[i] == 0:
            color[i] = color[node] * -1
            dfs(i)


for _ in range(k):
    answer = 'YES'
    v, e = map(int, input().split())

    maps = [[] for _ in range(v + 1)]
    color = [0] * (v + 1)
    color[1] = 1

    for i in range(1, e + 1):
        a, b = map(int, input().split())
        maps[a].append(b)
        maps[b].append(a)

    for i in range(1, v + 1):
        dfs(i)
    print(answer)
