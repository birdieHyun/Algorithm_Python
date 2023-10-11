N, M = map(int, input().split())

used = [False] * (N + 1)

def backtrack(cnt, s, start):
    if cnt == M:
        print(s.strip())

    for i in range(start, N + 1):
        if not used[i]:
            used[i] = True
            backtrack(cnt + 1, s + " " + str(i), i)
            used[i] = False

backtrack(0, "", 1)