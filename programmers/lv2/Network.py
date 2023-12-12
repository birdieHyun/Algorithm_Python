
def solution(n, computers):
    answer = 0

    visited = [False] * n

    for i in range(len(computers)):

        for j in range(len(computers)):
            if not visited[j]:
                dfs(j, computers, visited)
                answer += 1

    return answer


def dfs(start, computers, visited):

    if visited[start]:
        return

    visited[start] = True

    for i in range(len(computers)):
        if computers[start][i] == 1:
            dfs(i, computers, visited)