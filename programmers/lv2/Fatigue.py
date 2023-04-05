answer = 0
dungeon_length = 0
visited = []

def dfs(k, count, dungeons):
    global answer
    if count > answer:
        answer = count

    for i in range(dungeon_length):
        print(visited)
        if k>= dungeons[i][0] and not visited[i]:
            visited[i] = True
            print(visited)
            dfs(k - dungeons[i][1], count + 1, dungeons)
            visited[i] = False


def solution(k, dungeons):
    global dungeon_length, visited
    dungeon_length = len(dungeons)
    visited = [False] * dungeon_length
    dfs(k, 0, dungeons)
    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))
