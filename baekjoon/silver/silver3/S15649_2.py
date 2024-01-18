n, m = map(int, input().split())

visited = [False] * (n + 1)

def backtrack(depth, s):
    if depth == m:
        print(s.strip())
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            backtrack(depth + 1, s + ' ' + str(i))
            visited[i] =False

backtrack(0, "")